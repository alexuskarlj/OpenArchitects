# Import necessary modules and libraries
from flask import Blueprint, jsonify
from app import db
from app.models import User, Org, Logins, DashboardViews, Dashboard
from datetime import datetime
import humanize  # Import humanize library for time formatting
import re  # Import regular expressions library

# Create a Blueprint named 'routes'
bp = Blueprint('routes', __name__)

# Utility function to decode hex strings
def hex_to_str(hex_str):
    hex_str = str(hex_str)
    # Check if the string is a valid hexadecimal
    if re.fullmatch(r'[0-9a-fA-F]+', hex_str) is None:
        return "Invalid hexadecimal data"
    try:
        return bytes.fromhex(hex_str).decode('utf-8')
    except ValueError as e:
        return f"Error decoding hex: {e}"

# Utility function to calculate time ago
def time_ago(time):
    return humanize.naturaltime(datetime.utcnow() - time)

# Define a route '/recent_logins' to fetch recent login data
@bp.route('/recent_logins', methods=['GET'])
def recent_logins():
    try:
        # Query the database to fetch recent login data
        recent_logins_data = db.session.query(
            User.fname, User.lname, Org.name, Logins.timestamp
        ).join(User, User.id == Logins.user_id
        ).join(Org, Org.id == User.org
        ).order_by(Logins.timestamp.desc()).limit(10).all()

        # Format the data into a JSON response
        logins = [
            {
                'name': f"{hex_to_str(login[0])} {hex_to_str(login[1])}", 
                'organization': hex_to_str(login[2]), 
                'timestamp': time_ago(login[3])
            }
            for login in recent_logins_data
        ]

        return jsonify(logins)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route '/recent_dashboard_views' to fetch recent dashboard views data
@bp.route('/recent_dashboard_views', methods=['GET'])
def recent_dashboard_views():
    try:
        # Query the database to fetch recent dashboard views data
        recent_views_data = db.session.query(
            User.fname, User.lname, Org.name, DashboardViews.timestamp, Dashboard.title
        ).join(User, User.id == DashboardViews.user_id
        ).join(Org, Org.id == DashboardViews.user_org
        ).join(Dashboard, Dashboard.id == DashboardViews.dashboard_id
        ).order_by(DashboardViews.timestamp.desc()
        ).limit(10).all()

        # Format the data into a JSON response
        views = [
            {
                'name': f"{view[0]} {view[1]}",
                'organization': view[2],
                'dashboard': view[4],
                'timestamp': time_ago(view[3])
            }
            for view in recent_views_data
        ]

        return jsonify(views)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Define a route '/dashboard_stats' to fetch statistics about the dashboard
@bp.route('/dashboard_stats', methods=['GET'])
def dashboard_stats():
    try:
        # Calculate counts from the database
        dashboard_count = Dashboard.query.count()
        user_count = User.query.count()
        org_count = Org.query.count()
        login_count = Logins.query.count()
        view_count = DashboardViews.query.count()

        # Create a dictionary with the counts
        stats = {
            'dashboard_count': dashboard_count,
            'user_count': user_count,
            'org_count': org_count,
            'login_count': login_count,
            'view_count': view_count
        }

        return jsonify(stats)
    except Exception as e:
        return jsonify({'error': str(e)}), 500
