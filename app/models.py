from flask_login import UserMixin
from app import db

class User(UserMixin, db.Model):
	id = db.Column(db.Integer, primary_key=True)	
	email = db.Column(db.String(120), index=True, unique=True)
	password_hash = db.Column(db.String(128))
	fname = db.Column(db.String(120))
	lname = db.Column(db.String(120))
	org = db.Column(db.Integer, db.ForeignKey('org.id'))
	role = db.Column(db.String(120))
	disabled = db.Column(db.Boolean())
	admin = db.Column(db.Boolean())
	last_login = db.Column(db.DateTime)
	dashboard_views = db.relationship('DashboardViews', backref='dashboard_user_views', lazy='dynamic')	
	photo = db.Column(db.String(255))
	signin_method_override = db.Column(db.String(255))
	logins = db.relationship('Logins', backref='logins_user_data', lazy='dynamic')
	dashboard_modifications = db.relationship('Dashboard', backref='dashboard_edit_user_data', lazy='dynamic')
	local_id = db.Column(db.String(120))
	warehouse = db.Column(db.Boolean())

	def __repr__(self):
		return '<User {}>'.format(self.email)  

class Org(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(120))
	workspace_id = db.Column(db.String(120))
	leaders = db.Column(db.String(255))
	signin_method = db.Column(db.String(255))
	portal_version = db.Column(db.Integer)
	permissions_table = db.Column(db.String(255))
	dashboards = db.relationship('Dashboard', backref='owner', lazy='dynamic')
	users = db.relationship('User', backref="org_data", lazy='dynamic')
	dashboard_views = db.relationship('DashboardViews', backref='org_data', lazy='dynamic')
	schools = db.relationship('Schools', backref='org_data', lazy='dynamic')
	teacher_rostering = db.Column(db.Boolean())
	blob_path = db.Column(db.String(255))
	teacher_roles = db.Column(db.String(255))
	email_domain = db.Column(db.String(255))
	sis = db.Column(db.String(255))

	def __repr__(self):
		return '<Org {}>'.format(self.name)

class Dashboard(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	org_owner = db.Column(db.Integer, db.ForeignKey('org.id'))
	slug = db.Column(db.String(120))
	title = db.Column(db.String(120))
	description = db.Column(db.String(255))
	powerbi_report_id = db.Column(db.String(120))
	permissions = db.Column(db.String(255))
	image = db.Column(db.String(255))
	rls = db.Column(db.Boolean())
	rls_dataset_id = db.Column(db.String(255))
	category = db.Column(db.String(255))
	asset_type = db.Column(db.String(255))
	disabled = db.Column(db.Boolean())
	last_modified = db.Column(db.DateTime)
	last_modified_user = db.Column(db.Integer, db.ForeignKey('user.id'))
	dashboard_views = db.relationship('DashboardViews', backref='dashboard_views', lazy='dynamic')

	def __repr__(self):
		return '<Dashboard {}>'.format(self.title)

class Logins(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime)
	ip_address = db.Column(db.String(120))
	platform = db.Column(db.String(120))
	browser = db.Column(db.String(120))
	string = db.Column(db.String(255))
	email = db.Column(db.String(120))
	org = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	login_type = db.Column(db.String(255))
	result = db.Column(db.String(120))
	user_input = db.Column(db.String())
	ip_info = db.Column(db.String())

	def __repr__(self):
		return '<Login {}>'.format(self.timestamp)

class DashboardViews(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	timestamp = db.Column(db.DateTime)
	ip_address = db.Column(db.String(120))
	platform = db.Column(db.String(120))
	browser = db.Column(db.String(120))
	string = db.Column(db.String(255))
	email = db.Column(db.String(120))
	user_org = db.Column(db.Integer)
	user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
	dashboard_org = db.Column(db.Integer, db.ForeignKey('org.id'))
	dashboard_id = db.Column(db.Integer, db.ForeignKey('dashboard.id'))

	def __repr__(self):
		return '<View {}>'.format(self.timestamp)

class Schools(db.Model):
	school_id = db.Column(db.Integer, primary_key=True)
	local_school_id = db.Column(db.String())
	state_school_id = db.Column(db.String())
	school_name = db.Column(db.String())
	org = db.Column(db.Integer, db.ForeignKey('org.id'))
	permissions = db.Column(db.String())
	disabled = db.Column(db.Boolean())

	def __repr__(self):
		return '<School {} in {}>'.format(self.school_name, self.org_data.name)