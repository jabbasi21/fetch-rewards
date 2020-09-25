import flask

app = flask.Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	# Dynamically display number of unique email addresses on front page
	context = {}
	context['count'] = 0

	# Accept a list of email addresses and return an integer indicating the number of unique email addresses.
	if flask.request.method == 'POST':
		emails = list(flask.request.form['emails'].split(', '))

		# Unique email addresses means they will be delivered to the same account using Gmail account matching. 
		# Specifically: Gmail will ignore the placement of "." in the username. 
		# And it will ignore any portion of the username after a "+".
		count = 0
		for email in emails: 
			at_idx = email.find('@')
			username = email[:at_idx]

			username = username.replace('.', '')
			plus_idx = username.find('+')
			if plus_idx != -1:
				username = username[:plus_idx]

			new_email = username + email[at_idx:]
			emails[count] = new_email
			count += 1
		
		unique_emails = set(emails)
		context['count'] = len(unique_emails)

	return flask.render_template('index.html', **context)
