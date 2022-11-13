grammar Expr;
 
prog: expr EOF;
 
expr: op=('+'|'-') number=expr  cat=('rent'|'utilities'|'grocery')
    | COST                                   
    ;
 
OP_ADD: '+';
OP_SUB: '-';
command: 'list';
CAT_RENT: 'rent';
CAT_UTIL: 'utilities';
CAT_GROCERY: 'grocery';

NEWLINE : [\r\n]+ ;
COST     : [0-9]+[.]?[0-9]* ;
WS      : [ \t\r\n] -> channel(HIDDEN);
