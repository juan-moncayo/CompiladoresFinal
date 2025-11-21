grammar ScriptLang;

// Un programa tiene una o más escenas
program : scene+ EOF ;

// Una escena: escena nombre { dialogos }
scene : 'escena' ID '{' dialogue+ '}' ;

// Un diálogo puede ser decir u opcion
dialogue : sayStmt | optionStmt ;

// Instrucción decir: decir "texto";
sayStmt : 'decir' STRING ';' ;

// Instrucción opción: opcion "texto" ir_a destino;
optionStmt : 'opcion' STRING 'ir_a' ID ';' ;


// tokens
// Identificador: empieza con letra o _, puede tener números
ID : [a-zA-Z_][a-zA-Z_0-9]* ;

// String: texto entre comillas dobles
STRING : '"' (~["\r\n])* '"' ;

// Ignorar espacios y saltos de línea
WS : [ \t\r\n]+ -> skip ;

// Ignorar comentarios de línea // ...
LINE_COMMENT : '//' ~[\r\n]* -> skip ;

// Ignorar comentarios de bloque /* ... */
BLOCK_COMMENT : '/*' .*? '*/' -> skip ;