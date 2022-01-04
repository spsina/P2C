
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'nonassocGTEGTLTELTEQUNEQUANDORleftPLUSMINUSleftTIMESDIVMODrightUMINUSUPLUSAND BREAK COLON COMMENTS CONTINUE DIV DIV_EQUAL ELIF ELSE EQ EQU FALSE FOR GT GTE ID IF IN LBRACE LPRAN LT LTE MINUS MINUS_EQUAL MOD NEQU NOT NUMBER OR PLUS PLUS_EQUAL PRINT RANGE RBRACE RPRAN SEP STRING_LITERAL TIMES TIMES_EQUAL TRUE WHILE\n        statements : statements statement\n        | empty\n        \n        statement : assignment\n                    | if\n                    | while\n                    | for\n                    | expr\n                    | print\n                    | CONTINUE\n                    | BREAK\n        \n        print : PRINT LPRAN STRING_LITERAL print_args RPRAN\n        \n        print_args : expr\n                    | empty\n        \n        for : FOR ID IN RANGE LPRAN params RPRAN COLON LBRACE statements RBRACE\n        \n        params : num_or_id\n            |   num_or_id SEP num_or_id\n            | num_or_id SEP num_or_id SEP num_or_id\n        \n        while : WHILE expr COLON LBRACE statements RBRACE\n        \n        if : IF expr COLON LBRACE statements RBRACE elif\n        \n        elif : ELIF expr COLON LBRACE statements RBRACE elif\n        | else\n        \n        else : ELSE COLON LBRACE statements RBRACE\n        | empty\n        \n        assignment : ID EQ expr\n                   | ID PLUS_EQUAL expr\n                   | ID MINUS_EQUAL expr\n                   | ID TIMES_EQUAL expr\n                   | ID DIV_EQUAL expr\n        \n         expr : MINUS expr %prec UMINUS\n        \n         expr : PLUS expr %prec UPLUS\n        \n        expr : expr PLUS expr\n        | expr MINUS expr\n        | expr TIMES expr\n        | expr DIV expr\n        | expr MOD expr\n        | expr AND expr\n        | expr OR expr\n        | expr LT expr\n        | expr LTE expr\n        | expr GT expr\n        | expr GTE expr\n        | expr EQU expr\n        | expr NEQU expr\n        | ID\n        | NUMBER\n        | TRUE\n        | FALSE\n        \n        expr : LPRAN expr RPRAN\n\n        \n        num_or_id : NUMBER\n                | ID\n        empty :'
    
_lr_action_items = {'CONTINUE':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,72,73,78,79,81,82,83,88,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,10,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-51,-51,10,10,-11,-51,-18,-19,-21,-23,-51,-51,-51,10,10,10,-22,-14,-51,-20,]),'BREAK':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,72,73,78,79,81,82,83,88,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,11,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-51,-51,11,11,-11,-51,-18,-19,-21,-23,-51,-51,-51,11,11,11,-22,-14,-51,-20,]),'ID':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,78,79,80,81,82,83,88,89,90,92,94,100,101,102,103,104,105,107,108,109,110,111,],[-51,12,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,42,42,44,42,42,42,-45,-46,-47,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,42,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,42,-51,-51,12,12,84,-11,-51,-18,-19,42,-21,-23,84,-51,-51,84,-51,12,12,12,-22,-14,-51,-20,]),'IF':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,72,73,78,79,81,82,83,88,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,13,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-51,-51,13,13,-11,-51,-18,-19,-21,-23,-51,-51,-51,13,13,13,-22,-14,-51,-20,]),'WHILE':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,72,73,78,79,81,82,83,88,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,14,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-51,-51,14,14,-11,-51,-18,-19,-21,-23,-51,-51,-51,14,14,14,-22,-14,-51,-20,]),'FOR':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,72,73,78,79,81,82,83,88,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,15,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-51,-51,15,15,-11,-51,-18,-19,-21,-23,-51,-51,-51,15,15,15,-22,-14,-51,-20,]),'MINUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,76,78,79,81,82,83,88,89,90,92,95,100,101,103,104,105,107,108,109,110,111,],[-51,17,-2,-1,-3,-4,-5,-6,24,-8,-9,-10,-44,17,17,17,17,17,-45,-46,-47,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,24,-44,24,24,-29,-30,-31,-32,-33,-34,-35,24,24,24,24,24,24,24,24,24,24,24,24,24,-48,17,-51,-51,24,17,17,-11,-51,-18,-19,17,-21,-23,24,-51,-51,-51,17,17,17,-22,-14,-51,-20,]),'PLUS':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,76,78,79,81,82,83,88,89,90,92,95,100,101,103,104,105,107,108,109,110,111,],[-51,18,-2,-1,-3,-4,-5,-6,23,-8,-9,-10,-44,18,18,18,18,18,-45,-46,-47,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,18,23,-44,23,23,-29,-30,-31,-32,-33,-34,-35,23,23,23,23,23,23,23,23,23,23,23,23,23,-48,18,-51,-51,23,18,18,-11,-51,-18,-19,18,-21,-23,23,-51,-51,-51,18,18,18,-22,-14,-51,-20,]),'NUMBER':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,78,79,80,81,82,83,88,89,90,92,94,100,101,102,103,104,105,107,108,109,110,111,],[-51,19,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,19,19,19,19,19,-45,-46,-47,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,19,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,19,-51,-51,19,19,87,-11,-51,-18,-19,19,-21,-23,87,-51,-51,87,-51,19,19,19,-22,-14,-51,-20,]),'TRUE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,78,79,81,82,83,88,89,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,20,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,20,20,20,20,20,-45,-46,-47,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,20,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,20,-51,-51,20,20,-11,-51,-18,-19,20,-21,-23,-51,-51,-51,20,20,20,-22,-14,-51,-20,]),'FALSE':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,78,79,81,82,83,88,89,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,21,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,21,21,21,21,21,-45,-46,-47,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,21,-51,-51,21,21,-11,-51,-18,-19,21,-21,-23,-51,-51,-51,21,21,21,-22,-14,-51,-20,]),'LPRAN':([0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,71,72,73,74,78,79,81,82,83,88,89,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,16,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,16,16,16,16,16,-45,-46,-47,48,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,16,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,16,-51,-51,80,16,16,-11,-51,-18,-19,16,-21,-23,-51,-51,-51,16,16,16,-22,-14,-51,-20,]),'PRINT':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,72,73,78,79,81,82,83,88,90,92,100,101,103,104,105,107,108,109,110,111,],[-51,22,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-51,-51,22,22,-11,-51,-18,-19,-21,-23,-51,-51,-51,22,22,22,-22,-14,-51,-20,]),'$end':([0,1,2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,81,82,83,88,90,92,108,109,110,111,],[-51,0,-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-11,-51,-18,-19,-21,-23,-22,-14,-51,-20,]),'RBRACE':([2,3,4,5,6,7,8,9,10,11,12,19,20,21,42,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,72,73,78,79,81,82,83,88,90,92,100,101,103,104,105,107,108,109,110,111,],[-2,-1,-3,-4,-5,-6,-7,-8,-9,-10,-44,-45,-46,-47,-44,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-24,-25,-26,-27,-28,-48,-51,-51,82,83,-11,-51,-18,-19,-21,-23,-51,-51,-51,108,109,110,-22,-14,-51,-20,]),'TIMES':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[25,-44,-45,-46,-47,25,-44,25,25,-29,-30,25,25,-33,-34,-35,25,25,25,25,25,25,25,25,25,25,25,25,25,-48,25,25,]),'DIV':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[26,-44,-45,-46,-47,26,-44,26,26,-29,-30,26,26,-33,-34,-35,26,26,26,26,26,26,26,26,26,26,26,26,26,-48,26,26,]),'MOD':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[27,-44,-45,-46,-47,27,-44,27,27,-29,-30,27,27,-33,-34,-35,27,27,27,27,27,27,27,27,27,27,27,27,27,-48,27,27,]),'AND':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[28,-44,-45,-46,-47,28,-44,28,28,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,28,28,28,28,28,-48,28,28,]),'OR':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[29,-44,-45,-46,-47,29,-44,29,29,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,29,29,29,29,29,-48,29,29,]),'LT':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[30,-44,-45,-46,-47,30,-44,30,30,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,30,30,30,30,30,-48,30,30,]),'LTE':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[31,-44,-45,-46,-47,31,-44,31,31,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,31,31,31,31,31,-48,31,31,]),'GT':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[32,-44,-45,-46,-47,32,-44,32,32,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,32,32,32,32,32,-48,32,32,]),'GTE':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[33,-44,-45,-46,-47,33,-44,33,33,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,33,33,33,33,33,-48,33,33,]),'EQU':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[34,-44,-45,-46,-47,34,-44,34,34,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,34,34,34,34,34,-48,34,34,]),'NEQU':([8,12,19,20,21,41,42,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,70,76,95,],[35,-44,-45,-46,-47,35,-44,35,35,-29,-30,-31,-32,-33,-34,-35,None,None,None,None,None,None,None,None,35,35,35,35,35,-48,35,35,]),'EQ':([12,],[36,]),'PLUS_EQUAL':([12,],[37,]),'MINUS_EQUAL':([12,],[38,]),'TIMES_EQUAL':([12,],[39,]),'DIV_EQUAL':([12,],[40,]),'COLON':([19,20,21,41,42,43,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,70,91,93,95,],[-45,-46,-47,67,-44,68,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-48,96,97,99,]),'RPRAN':([19,20,21,42,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,70,71,75,76,77,84,85,86,87,98,106,],[-45,-46,-47,-44,70,-29,-30,-31,-32,-33,-34,-35,-36,-37,-38,-39,-40,-41,-42,-43,-48,-51,81,-12,-13,-50,93,-15,-49,-16,-17,]),'IN':([44,],[69,]),'STRING_LITERAL':([48,],[71,]),'LBRACE':([67,68,96,97,99,],[72,73,100,101,103,]),'RANGE':([69,],[74,]),'ELIF':([82,110,],[89,89,]),'ELSE':([82,110,],[91,91,]),'SEP':([84,86,87,98,],[-50,94,-49,102,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'statements':([0,72,73,100,101,103,],[1,78,79,104,105,107,]),'empty':([0,71,72,73,82,100,101,103,110,],[2,77,2,2,92,2,2,2,92,]),'statement':([1,78,79,104,105,107,],[3,3,3,3,3,3,]),'assignment':([1,78,79,104,105,107,],[4,4,4,4,4,4,]),'if':([1,78,79,104,105,107,],[5,5,5,5,5,5,]),'while':([1,78,79,104,105,107,],[6,6,6,6,6,6,]),'for':([1,78,79,104,105,107,],[7,7,7,7,7,7,]),'expr':([1,13,14,16,17,18,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,71,78,79,89,104,105,107,],[8,41,43,45,46,47,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,65,66,76,8,8,95,8,8,8,]),'print':([1,78,79,104,105,107,],[9,9,9,9,9,9,]),'print_args':([71,],[75,]),'params':([80,],[85,]),'num_or_id':([80,94,102,],[86,98,106,]),'elif':([82,110,],[88,111,]),'else':([82,110,],[90,90,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> statements","S'",1,None,None,None),
  ('statements -> statements statement','statements',2,'p_statements','parser.py',48),
  ('statements -> empty','statements',1,'p_statements','parser.py',49),
  ('statement -> assignment','statement',1,'p_statement','parser.py',59),
  ('statement -> if','statement',1,'p_statement','parser.py',60),
  ('statement -> while','statement',1,'p_statement','parser.py',61),
  ('statement -> for','statement',1,'p_statement','parser.py',62),
  ('statement -> expr','statement',1,'p_statement','parser.py',63),
  ('statement -> print','statement',1,'p_statement','parser.py',64),
  ('statement -> CONTINUE','statement',1,'p_statement','parser.py',65),
  ('statement -> BREAK','statement',1,'p_statement','parser.py',66),
  ('print -> PRINT LPRAN STRING_LITERAL print_args RPRAN','print',5,'p_print','parser.py',72),
  ('print_args -> expr','print_args',1,'p_print_args','parser.py',78),
  ('print_args -> empty','print_args',1,'p_print_args','parser.py',79),
  ('for -> FOR ID IN RANGE LPRAN params RPRAN COLON LBRACE statements RBRACE','for',11,'p_for','parser.py',85),
  ('params -> num_or_id','params',1,'p_params','parser.py',91),
  ('params -> num_or_id SEP num_or_id','params',3,'p_params','parser.py',92),
  ('params -> num_or_id SEP num_or_id SEP num_or_id','params',5,'p_params','parser.py',93),
  ('while -> WHILE expr COLON LBRACE statements RBRACE','while',6,'p_while','parser.py',104),
  ('if -> IF expr COLON LBRACE statements RBRACE elif','if',7,'p_if','parser.py',110),
  ('elif -> ELIF expr COLON LBRACE statements RBRACE elif','elif',7,'p_elif','parser.py',116),
  ('elif -> else','elif',1,'p_elif','parser.py',117),
  ('else -> ELSE COLON LBRACE statements RBRACE','else',5,'p_else','parser.py',126),
  ('else -> empty','else',1,'p_else','parser.py',127),
  ('assignment -> ID EQ expr','assignment',3,'p_assignment','parser.py',134),
  ('assignment -> ID PLUS_EQUAL expr','assignment',3,'p_assignment','parser.py',135),
  ('assignment -> ID MINUS_EQUAL expr','assignment',3,'p_assignment','parser.py',136),
  ('assignment -> ID TIMES_EQUAL expr','assignment',3,'p_assignment','parser.py',137),
  ('assignment -> ID DIV_EQUAL expr','assignment',3,'p_assignment','parser.py',138),
  ('expr -> MINUS expr','expr',2,'p_exr_unary_minus','parser.py',144),
  ('expr -> PLUS expr','expr',2,'p_exr_unary_plus','parser.py',150),
  ('expr -> expr PLUS expr','expr',3,'p_expr_operator_relop','parser.py',156),
  ('expr -> expr MINUS expr','expr',3,'p_expr_operator_relop','parser.py',157),
  ('expr -> expr TIMES expr','expr',3,'p_expr_operator_relop','parser.py',158),
  ('expr -> expr DIV expr','expr',3,'p_expr_operator_relop','parser.py',159),
  ('expr -> expr MOD expr','expr',3,'p_expr_operator_relop','parser.py',160),
  ('expr -> expr AND expr','expr',3,'p_expr_operator_relop','parser.py',161),
  ('expr -> expr OR expr','expr',3,'p_expr_operator_relop','parser.py',162),
  ('expr -> expr LT expr','expr',3,'p_expr_operator_relop','parser.py',163),
  ('expr -> expr LTE expr','expr',3,'p_expr_operator_relop','parser.py',164),
  ('expr -> expr GT expr','expr',3,'p_expr_operator_relop','parser.py',165),
  ('expr -> expr GTE expr','expr',3,'p_expr_operator_relop','parser.py',166),
  ('expr -> expr EQU expr','expr',3,'p_expr_operator_relop','parser.py',167),
  ('expr -> expr NEQU expr','expr',3,'p_expr_operator_relop','parser.py',168),
  ('expr -> ID','expr',1,'p_expr_operator_relop','parser.py',169),
  ('expr -> NUMBER','expr',1,'p_expr_operator_relop','parser.py',170),
  ('expr -> TRUE','expr',1,'p_expr_operator_relop','parser.py',171),
  ('expr -> FALSE','expr',1,'p_expr_operator_relop','parser.py',172),
  ('expr -> LPRAN expr RPRAN','expr',3,'p_expr_pran','parser.py',181),
  ('num_or_id -> NUMBER','num_or_id',1,'p_num_or_id','parser.py',188),
  ('num_or_id -> ID','num_or_id',1,'p_num_or_id','parser.py',189),
  ('empty -> <empty>','empty',0,'p_empty','parser.py',194),
]
