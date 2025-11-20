grammar ScriptLang;

program : scene+ EOF ;
scene : 'escena' ID '{' dialogue+ '}' ;
dialogue : sayStmt | optionStmt ;
sayStmt : 'decir' STRING ';' ;
optionStmt : 'opcion' STRING 'ir_a' ID ';' ;

ID : [a-zA-Z_][a-zA-Z_0-9]* ;
STRING : '"' (~["\r\n])* '"' ;
WS : [ \t\r\n]+ -> skip ;
LINE_COMMENT : '//' ~[\r\n]* -> skip ;
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;
