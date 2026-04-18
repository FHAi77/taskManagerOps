from flask import Flask, render_template, request, jsonify
import sqlite3
from datetime import datetime, timedelta
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'task-manager-secret-key'

def get_db():
    conn = sqlite3.connect('tasks.db')
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    conn = get_db()
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS tasks
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  title TEXT NOT NULL,
                  description TEXT,
                  priority INTEGER DEFAULT 1,
                  category TEXT,
                  tags TEXT,
                  status TEXT DEFAULT 'pending',
                  start_date TEXT,
                  end_date TEXT,
                  created_at TEXT DEFAULT CURRENT_TIMESTAMP)''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS categories
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  color TEXT DEFAULT '#3B82F6')''')
    
    c.execute('''CREATE TABLE IF NOT EXISTS tags
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                  name TEXT NOT NULL,
                  color TEXT DEFAULT '#6B7280')''')
    
    conn.commit()
    conn.close()

def generate_mock_data():
    conn = get_db()
    c = conn.cursor()
    
    c.execute('SELECT COUNT(*) FROM tasks')
    if c.fetchone()[0] > 0:
        conn.close()
        return
    
    categories = [
        ('工作', '#3B82F6'),
        ('个人', '#10B981'),
        ('学习', '#8B5CF6'),
        ('健康', '#F59E0B'),
        ('其他', '#6B7280')
    ]
    for name, color in categories:
        c.execute('INSERT INTO categories (name, color) VALUES (?, ?)', (name, color))
    
    tags = [
        ('紧急', '#EF4444'),
        ('重要', '#F59E0B'),
        ('会议', '#8B5CF6'),
        ('文档', '#3B82F6'),
        ('待审核', '#10B981')
    ]
    for name, color in tags:
        c.execute('INSERT INTO tags (name, color) VALUES (?, ?)', (name, color))
    
    task_titles = [
        ('完成项目报告', 3, '工作', '重要,文档', '完成'),
        ('团队周会', 2, '工作', '会议', '进行中'),
        ('学习Python高级特性', 1, '学习', '文档', '待处理'),
        ('健身计划', 2, '健康', '重要', '待处理'),
        ('代码审查', 3, '工作', '待审核,紧急', '进行中'),
        ('阅读技术文档', 1, '学习', '文档', '完成'),
        ('更新个人简历', 2, '个人', '重要', '待处理'),
        ('数据库优化', 3, '工作', '紧急,重要', '完成'),
        ('UI设计评审', 2, '工作', '会议', '待处理'),
        ('每日跑步', 1, '健康', '', '进行中')
    ]
    
    base_date = datetime.now()
    for i, (title, priority, category, tags, status) in enumerate(task_titles):
        start_date = (base_date + timedelta(days=random.randint(-10, 10))).strftime('%Y-%m-%d')
        end_date = (base_date + timedelta(days=random.randint(0, 14))).strftime('%Y-%m-%d')
        c.execute('''INSERT INTO tasks (title, description, priority, category, tags, status, start_date, end_date)
                     VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                  (title, f'{title}的详细描述...', priority, category, tags, status, start_date, end_date))
    
    conn.commit()
    conn.close()

translations = {
    'zh': {
        'app_name': '日程任务管理',
        'task_list': '任务列表',
        'calendar': '日历视图',
        'categories': '分类标签',
        'statistics': '任务统计',
        'add_task': '新增任务',
        'edit_task': '编辑任务',
        'delete_task': '删除任务',
        'task_title': '任务标题',
        'description': '任务描述',
        'priority': '优先级',
        'category': '分类',
        'tags': '标签',
        'status': '状态',
        'start_date': '开始日期',
        'end_date': '结束日期',
        'actions': '操作',
        'save': '保存',
        'cancel': '取消',
        'delete': '删除',
        'edit': '编辑',
        'pending': '待处理',
        'in_progress': '进行中',
        'completed': '完成',
        'high': '高',
        'medium': '中',
        'low': '低',
        'month_view': '月视图',
        'week_view': '周视图',
        'today': '今天',
        'completion_rate': '任务完成率',
        'monthly_stats': '月度工作统计',
        'total_tasks': '总任务数',
        'completed_tasks': '已完成',
        'pending_tasks': '待处理',
        'filter_by_category': '按分类筛选',
        'filter_by_tag': '按标签筛选',
        'all_categories': '全部分类',
        'all_tags': '全部标签',
        'language': '语言',
        'confirm_delete': '确认删除此任务？',
        'no_tasks': '暂无任务',
        'drag_to_adjust': '拖拽调整任务时间'
    },
    'en': {
        'app_name': 'Task Manager',
        'task_list': 'Task List',
        'calendar': 'Calendar',
        'categories': 'Categories',
        'statistics': 'Statistics',
        'add_task': 'Add Task',
        'edit_task': 'Edit Task',
        'delete_task': 'Delete Task',
        'task_title': 'Task Title',
        'description': 'Description',
        'priority': 'Priority',
        'category': 'Category',
        'tags': 'Tags',
        'status': 'Status',
        'start_date': 'Start Date',
        'end_date': 'End Date',
        'actions': 'Actions',
        'save': 'Save',
        'cancel': 'Cancel',
        'delete': 'Delete',
        'edit': 'Edit',
        'pending': 'Pending',
        'in_progress': 'In Progress',
        'completed': 'Completed',
        'high': 'High',
        'medium': 'Medium',
        'low': 'Low',
        'month_view': 'Month',
        'week_view': 'Week',
        'today': 'Today',
        'completion_rate': 'Completion Rate',
        'monthly_stats': 'Monthly Statistics',
        'total_tasks': 'Total Tasks',
        'completed_tasks': 'Completed',
        'pending_tasks': 'Pending',
        'filter_by_category': 'Filter by Category',
        'filter_by_tag': 'Filter by Tag',
        'all_categories': 'All Categories',
        'all_tags': 'All Tags',
        'language': 'Language',
        'confirm_delete': 'Confirm delete this task?',
        'no_tasks': 'No tasks',
        'drag_to_adjust': 'Drag to adjust dates'
    }
}

@app.context_processor
def inject_translations():
    lang = request.cookies.get('lang', 'zh')
    return dict(t=translations[lang], current_lang=lang, datetime=datetime)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    conn = get_db()
    tasks = conn.execute('SELECT * FROM tasks ORDER BY priority DESC, start_date').fetchall()
    conn.close()
    return jsonify([dict(t) for t in tasks])

@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.json
    conn = get_db()
    c = conn.cursor()
    c.execute('''INSERT INTO tasks (title, description, priority, category, tags, status, start_date, end_date)
                 VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
              (data['title'], data.get('description', ''), data['priority'], 
               data.get('category', ''), data.get('tags', ''), data.get('status', 'pending'),
               data.get('start_date', ''), data.get('end_date', '')))
    conn.commit()
    task_id = c.lastrowid
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return jsonify(dict(task))

@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    data = request.json
    conn = get_db()
    conn.execute('''UPDATE tasks SET title=?, description=?, priority=?, category=?, 
                    tags=?, status=?, start_date=?, end_date=? WHERE id=?''',
                 (data['title'], data.get('description', ''), data['priority'],
                  data.get('category', ''), data.get('tags', ''), data.get('status', 'pending'),
                  data.get('start_date', ''), data.get('end_date', ''), task_id))
    conn.commit()
    task = conn.execute('SELECT * FROM tasks WHERE id = ?', (task_id,)).fetchone()
    conn.close()
    return jsonify(dict(task))

@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    conn = get_db()
    conn.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/api/categories', methods=['GET'])
def get_categories():
    conn = get_db()
    categories = conn.execute('SELECT * FROM categories').fetchall()
    conn.close()
    return jsonify([dict(c) for c in categories])

@app.route('/api/tags', methods=['GET'])
def get_tags():
    conn = get_db()
    tags = conn.execute('SELECT * FROM tags').fetchall()
    conn.close()
    return jsonify([dict(t) for t in tags])

@app.route('/api/statistics')
def get_statistics():
    conn = get_db()
    total = conn.execute('SELECT COUNT(*) FROM tasks').fetchone()[0]
    completed = conn.execute('SELECT COUNT(*) FROM tasks WHERE status = "完成" OR status = "Completed"').fetchone()[0]
    pending = conn.execute('SELECT COUNT(*) FROM tasks WHERE status = "待处理" OR status = "Pending"').fetchone()[0]
    in_progress = conn.execute('SELECT COUNT(*) FROM tasks WHERE status = "进行中" OR status = "In Progress"').fetchone()[0]
    
    monthly = []
    for i in range(6):
        month = (datetime.now() - timedelta(days=i*30)).strftime('%Y-%m')
        count = random.randint(5, 20)
        monthly.append({'month': month, 'count': count})
    
    conn.close()
    return jsonify({
        'total': total,
        'completed': completed,
        'pending': pending,
        'in_progress': in_progress,
        'completion_rate': round(completed / total * 100, 1) if total > 0 else 0,
        'monthly': monthly
    })

if __name__ == '__main__':
    init_db()
    generate_mock_data()
    app.run(debug=True, host='0.0.0.0', port=8080)
