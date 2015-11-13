
import sys
import re
import logging
logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO

inputs = []
outputs = []


def printException():
    exc_type, exc_obj, tb = sys.exc_info()
    print(exc_obj)  

def test(_file, _inputs, _outputs, _message = 'Not quite right please try again'):
  global outputs
  outputs = []
  
  global inputs
  inputs = _inputs
  
  try:
    # redirect stdout to a string (fake_stdout)                                      
    # compile into byte code and then execute the byte code                          
    # then process the printed output from the code we ran                           
    code= compile(open(_file).read(), '<string>', 'exec')                      
    orig_stdout= sys.stdout
    fake_stdout= StringIO()
    sys.stdout= fake_stdout

    # replace sys.argv while we exec the code
    orig_argv= sys.argv
    sys.argv= ['python', _file] 
    for i in range(0, len(inputs)):
      sys.argv.append(inputs[i])
    exec(code)

    # put everything back like it was before
    sys.stdout= orig_stdout
    sys.argv= orig_argv
    sys.stderr.flush()

    # set up the outputs
    outputs= fake_stdout.getvalue().split("\n")		
    last_line= outputs.pop()
    if len(last_line.strip()) > 0:
      outputs.append(last_line)

    #print(outputs)
    
    #
    # Display output for student
    # 
    # <br/><hr/><h3>Challenge Feedback</h3>
    #print('<div class="challenge-result">')
    #print('<br/><hr/><h3>Challenge Results</h3>')
    #print("<hr/>")
    
    outputText= '<div class="challenge-result">'
    outputText += '<br/><b>WRONG SCRIPT</b><hr/>'
    outputText += '<br/><b>Challenge Results</b><hr/>'
    outputText += '<small><b>Program Input: </b></small>' 
    outputText += '<br/>'
    outputText += str(inputs)
    outputText += '<br/>'
    outputText += '<small><b>Your Output: </b></small>'
    outputText += '<br/>'
    #outputText += '<hr/>'
    outputText += fake_stdout.getvalue()
    #outputText += '<hr/>'
    
    outputText += '<small><b>Feedback: </b></small>'
    outputText += '</div><br/>'
    
    print(outputText)

    if len(outputs) != len(_outputs):
      print('Your program is not outputting the expected number of outputs')
      exit(1)

    # print(outputs)
    # print(_outputs)
      
    for i in range(len(outputs)):
      if str(outputs[i]) != str(_outputs[i]):
        #print(str(outputs[i]) + " != " + str(_outputs[i]))
        print(_message)
        exit(1)
    
  except (IOError, SyntaxError, NameError) as e:
    printException()
    exit(1)
    
