grammar Expr;

prog: expr EOF;

expr: left=expr finance='CHECK'              #financecheckExpr         
    | left=expr finance=('ADD'|'SUB') right=expr #financeExpr
    | left=expr op='=' right=expr              #eqExpr
    | trig=('sin'|'cos'|'tan') right=expr      #trigExpr
    | func=('ln'|'e'|'log') right=expr         #funcExpr
    | left=expr op='^' right=expr              #infixExpr
    | left=expr op=('*'|'/') right=expr        #infixExpr
    | left=expr op=('+'|'-') right=expr        #infixExpr
    | NUM                                      #numberExpr
    | STR                                      #strExpr
    | '(' expr ')'                             #parensExpr
    ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_POW: '^';
OP_EQ: '=';
TRIG_SIN: 'sin';
TRIG_COS: 'cos';
TRIG_TAN: 'tan';
FUNC_E: 'e';
FUNC_LN: 'ln';
FUNC_LOG: 'log';
FINANCE_ADD: 'ADD';
FINANCE_SUB: 'SUB';
FINANCE_CHECK: 'CHECK';

NEWLINE : [\r\n]+ ;
NUM     : [0-9]+.?[0-9]* ;
STR     : [A-Za-z]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);
