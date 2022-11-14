grammar Expr;

prog: expr EOF;

expr: left=expr right=expr                #trigExpr
    | left=expr op='^' right=expr         #infixExpr
    | left=expr op=('*'|'/') right=expr   #infixExpr
    | left=expr op=('+'|'-') right=expr   #infixExpr
    | NUM                                 #numberExpr
    | STR                                 #strExpr
    | '(' expr ')'                        #parensExpr
    ;

OP_ADD: '+';
OP_SUB: '-';
OP_MUL: '*';
OP_DIV: '/';
OP_POW: '^';

NEWLINE : [\r\n]+ ;
NUM     : [0-9]+.?[0-9]* ;
STR     : [a-z]+ ;
WS      : [ \t\r\n] -> channel(HIDDEN);
