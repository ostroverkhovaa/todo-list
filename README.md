🧾 Django TODO List project

A clean and functional Django web app for managing your daily tasks with tagging, deadlines, and completion tracking.

📦 Features

- Full CRUD for:
  - Tasks
  - Tags
- Sidebar navigation across all pages
- Mark tasks as complete/incomplete
- Task sorting:
  - Incomplete tasks first
  - Newest tasks first
- Tag multiple tasks with many-to-many support
- Responsive layout

🛠 Tech Stack

- Python 3 & Django
- Bootstrap 4 + custom CSS
- Django Templates
- SQLite (default)

📁 Setup

1. Clone the repo
git clone https://github.com/ostroverkhovaa/todo-list.git
cd todo-list

2. Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate

3. Install dependencies
pip install -r requirements.txt

4. Run migrations
python manage.py migrate

5. Start the server
python manage.py runserver
