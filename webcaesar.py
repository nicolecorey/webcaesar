from flask import Flask, render_template, request

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
@app.route('/user_message', methods=['GET', 'POST'])
def user_message():
  original_message = ''
  coded_message = ''
  shift = 0
  code_action = ''
  if request.method == 'POST':
    shift = int(request.form['shift']) 
    code_action = request.form.get('code_action')
    original_message = request.form['message']
    coded_message = ''

  # if code_action == 'encrypt':
  #     coded_message = encrypt_message(original_message, shift)
  # elif code_action == 'decrypt':
  #     coded_message = decrypt_message(original_message, shift)
      
  return render_template('user_message.html',
                           original_message=original_message, 
                           coded_message=coded_message,
                           code_action=code_action, 
                           shift=shift)

if __name__ == '__main__':
    app.run()

# Instructions for this project can be found here:
# https://education.launchcode.org/lchs/chapters/flask-intro/project.html