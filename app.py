from flask import Flask, render_template, request, jsonify
from database import init_db, get_db
from datetime import datetime, timedelta
import calendar

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

# ── EXPENSES ──────────────────────────────────────────
@app.route('/api/expenses', methods=['GET'])
def get_expenses():
    db = get_db()
    search = request.args.get('search', '').lower()
    category = request.args.get('category', '')
    wallet = request.args.get('wallet', '')

    query = 'SELECT * FROM expenses WHERE 1=1'
    params = []
    if search:
        query += ' AND LOWER(title) LIKE ?'
        params.append(f'%{search}%')
    if category:
        query += ' AND category = ?'
        params.append(category)
    if wallet:
        query += ' AND wallet = ?'
        params.append(wallet)
    query += ' ORDER BY date DESC'

    expenses = db.execute(query, params).fetchall()
    db.close()
    return jsonify([dict(e) for e in expenses])

@app.route('/api/expenses', methods=['POST'])
def add_expense():
    data = request.json
    db = get_db()
    db.execute(
        'INSERT INTO expenses (title, amount, category, date, wallet, note, recurring) VALUES (?, ?, ?, ?, ?, ?, ?)',
        (data['title'], data['amount'], data['category'], data['date'],
         data.get('wallet', 'Cash'), data.get('note', ''), data.get('recurring', 0))
    )
    db.commit()
    db.close()
    return jsonify({'success': True})

@app.route('/api/expenses/<int:expense_id>', methods=['DELETE'])
def delete_expense(expense_id):
    db = get_db()
    db.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
    db.commit()
    db.close()
    return jsonify({'success': True})

# ── STATS ──────────────────────────────────────────────
@app.route('/api/stats', methods=['GET'])
def get_stats():
    db = get_db()
    today = datetime.now()
    month_start = today.replace(day=1).strftime('%Y-%m-%d')
    week_start = (today - timedelta(days=today.weekday())).strftime('%Y-%m-%d')

    month_total = db.execute('SELECT COALESCE(SUM(amount),0) as t FROM expenses WHERE date >= ?', (month_start,)).fetchone()['t']
    week_total  = db.execute('SELECT COALESCE(SUM(amount),0) as t FROM expenses WHERE date >= ?', (week_start,)).fetchone()['t']
    goals       = db.execute('SELECT * FROM savings_goal WHERE id=1').fetchone()
    categories  = db.execute('SELECT category, SUM(amount) as total FROM expenses WHERE date >= ? GROUP BY category', (month_start,)).fetchall()
    wallets     = db.execute('SELECT wallet, SUM(amount) as total FROM expenses WHERE date >= ? GROUP BY wallet', (month_start,)).fetchall()

    db.close()
    return jsonify({
        'month_total': month_total,
        'week_total': week_total,
        'budget': goals['monthly_budget'],
        'savings_target': goals['savings_target'],
        'categories': [dict(c) for c in categories],
        'wallets': [dict(w) for w in wallets]
    })
    # ── MONTHLY TREND ──────────────────────────────────────
@app.route('/api/trend', methods=['GET'])
def get_trend():
    db = get_db()
    today = datetime.now()
    result = []
    for i in range(5, -1, -1):
        d = today.replace(day=1) - timedelta(days=i*28)
        m_start = d.replace(day=1).strftime('%Y-%m-%d')
        last_day = calendar.monthrange(d.year, d.month)[1]
        m_end = d.replace(day=last_day).strftime('%Y-%m-%d')
        total = db.execute(
            'SELECT COALESCE(SUM(amount),0) as t FROM expenses WHERE date >= ? AND date <= ?',
            (m_start, m_end)
        ).fetchone()['t']
        result.append({'month': d.strftime('%b %Y'), 'total': total})
    db.close()
    return jsonify(result)

# ── GOALS ──────────────────────────────────────────────
@app.route('/api/goals', methods=['POST'])
def update_goals():
    data = request.json
    db = get_db()
    db.execute('UPDATE savings_goal SET monthly_budget=?, savings_target=? WHERE id=1',
               (data['budget'], data['savings_target']))
    db.commit()
    db.close()
    return jsonify({'success': True})

# ── PROFILE ────────────────────────────────────────────
@app.route('/api/profile', methods=['GET'])
def get_profile():
    db = get_db()
    p = db.execute('SELECT * FROM profile WHERE id=1').fetchone()
    db.close()
    return jsonify(dict(p))

@app.route('/api/profile', methods=['POST'])
def update_profile():
    data = request.json
    db = get_db()
    db.execute('UPDATE profile SET name=?, income=?, photo=? WHERE id=1',
               (data.get('name',''), data.get('income', 0), data.get('photo','')))
    db.commit()
    db.close()
    return jsonify({'success': True})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)