# punchie

![alt text](https://i.imgur.com/kbM4So0.png "Ibm_026_1949")

A project that handles ye old Punched cards based on http://homepage.divms.uiowa.edu/~jones/cards/codes.html.

Using Python2 you can transform strings to Punched cards (keypunches).

_I suggest you use a [Virtual Environment](https://virtualenv.pypa.io/en/stable/)._

### Execution
1. Set up the Python2 Virtual Environment.  
`virtualenv -p python2 venv`
2. Activate it.     
`source venv/bin/activate`  
3. Run the executable.  
`./punch <file> <format>`

_The formats are cdc, dec_026, dec_029, ge_600, ibm_024_rept, ibm_024_prog, ibm_026_fort, ibm_026_comm, ibm_029_029, ibm_029_ibme, ibm_029_ebcd, ibm_1401, univac_1108_

### Example
Run the example script.  
`./example.py`

Deactivate the Virtual Environment when you finish it.    
`deactivate`