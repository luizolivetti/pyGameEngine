#  ----------------------------------------------------------
#  Keyboard
#  Classe compoennte para controle do Keyboard  
#  ----------------------------------------------------------
#  @author  Luiz Olivetti     @data 31/12/2024
#  @revisor                   @data 
#  ----------------------------------------------------------
#  Fonte : https://www.pygame.org/docs/ref/key.html
#  ----------------------------------------------------------
#  K_BACKSPACE   \b      backspace
#  K_TAB         \t      tab
#  K_CLEAR               clear
#  K_RETURN      \r      return
#  K_PAUSE               pause
#  K_ESCAPE      ^[      escape
#  K_SPACE               space
#  K_EXCLAIM     !       exclaim
#  K_QUOTEDBL    "       quotedbl
#  K_HASH        #       hash
#  K_DOLLAR      $       dollar
#  K_AMPERSAND   &       ampersand
#  K_QUOTE               quote
#  K_LEFTPAREN   (       left parenthesis
#  K_RIGHTPAREN  )       right parenthesis
#  K_ASTERISK    *       asterisk
#  K_PLUS        +       plus sign
#  K_COMMA       ,       comma
#  K_MINUS       -       minus sign
#  K_PERIOD      .       period
#  K_SLASH       /       forward slash
#  K_0           0       0
#  K_1           1       1
#  K_2           2       2
#  K_3           3       3
#  K_4           4       4
#  K_5           5       5
#  K_6           6       6
#  K_7           7       7
#  K_8           8       8
#  K_9           9       9
#  K_COLON       :       colon
#  K_SEMICOLON   ;       semicolon
#  K_LESS        <       less-than sign
#  K_EQUALS      =       equals sign
#  K_GREATER     >       greater-than sign
#  K_QUESTION    ?       question mark
#  K_AT          @       at
#  K_LEFTBRACKET [       left bracket
#  K_BACKSLASH   \       backslash
#  K_RIGHTBRACKET ]      right bracket
#  K_CARET       ^       caret
#  K_UNDERSCORE  _       underscore
#  K_BACKQUOTE   `       grave
#  K_a           a       a
#  K_b           b       b
#  K_c           c       c
#  K_d           d       d
#  K_e           e       e
#  K_f           f       f
#  K_g           g       g
#  K_h           h       h
#  K_i           i       i
#  K_j           j       j
#  K_k           k       k
#  K_l           l       l
#  K_m           m       m
#  K_n           n       n
#  K_o           o       o
#  K_p           p       p
#  K_q           q       q
#  K_r           r       r
#  K_s           s       s
#  K_t           t       t
#  K_u           u       u
#  K_v           v       v
#  K_w           w       w
#  K_x           x       x
#  K_y           y       y
#  K_z           z       z
#  K_DELETE              delete
#  K_KP0                 keypad 0
#  K_KP1                 keypad 1
#  K_KP2                 keypad 2
#  K_KP3                 keypad 3
#  K_KP4                 keypad 4
#  K_KP5                 keypad 5
#  K_KP6                 keypad 6
#  K_KP7                 keypad 7
#  K_KP8                 keypad 8
#  K_KP9                 keypad 9
#  K_KP_PERIOD   .       keypad period
#  K_KP_DIVIDE   /       keypad divide
#  K_KP_MULTIPLY *       keypad multiply
#  K_KP_MINUS    -       keypad minus
#  K_KP_PLUS     +       keypad plus
#  K_KP_ENTER    \r      keypad enter
#  K_KP_EQUALS   =       keypad equals
#  K_UP                  up arrow
#  K_DOWN                down arrow
#  K_RIGHT               right arrow
#  K_LEFT                left arrow
#  K_INSERT              insert
#  K_HOME                home
#  K_END                 end
#  K_PAGEUP              page up
#  K_PAGEDOWN            page down
#  K_F1                  F1
#  K_F2                  F2
#  K_F3                  F3
#  K_F4                  F4
#  K_F5                  F5
#  K_F6                  F6
#  K_F7                  F7
#  K_F8                  F8
#  K_F9                  F9
#  K_F10                 F10
#  K_F11                 F11
#  K_F12                 F12
#  K_F13                 F13
#  K_F14                 F14
#  K_F15                 F15
#  K_NUMLOCK             numlock
#  K_CAPSLOCK            capslock
#  K_SCROLLOCK           scrollock
#  K_RSHIFT              right shift
#  K_LSHIFT              left shift
#  K_RCTRL               right control
#  K_LCTRL               left control
#  K_RALT                right alt
#  K_LALT                left alt
#  K_RMETA               right meta
#  K_LMETA               left meta
#  K_LSUPER              left Windows key
#  K_RSUPER              right Windows key
#  K_MODE                mode shift
#  K_HELP                help
#  K_PRINT               print screen
#  K_SYSREQ              sysrq
#  K_BREAK               break
#  K_MENU                menu
#  K_POWER               power
#  K_EURO                Euro
#  K_AC_BACK             Android back button
import pygame
#
# tools
#
from functools import partial
#
# interface
#
from pyGameEngine.components.extends.input.device import device
#
# Class keyboard
#
class keyboard(device):
    #
    # __init__
    #
    def __init__(self):
        self.BACKSPACE  = pygame.K_BACKSPACE  
        self.TAB        = pygame.K_TAB         
        self.CLEAR      = pygame.K_CLEAR       
        self.RETURN     = pygame.K_RETURN      
        self.PAUSE      = pygame.K_PAUSE       
        self.ESCAPE     = pygame.K_ESCAPE      
        self.SPACE      = pygame.K_SPACE       
        self.EXCLAIM    = pygame.K_EXCLAIM     
        self.QUOTEDBL   = pygame.K_QUOTEDBL    
        self.HASH       = pygame.K_HASH        
        self.DOLLAR     = pygame.K_DOLLAR      
        self.AMPERSAND  = pygame.K_AMPERSAND   
        self.QUOTE      = pygame.K_QUOTE       
        self.LEFTPAREN  = pygame.K_LEFTPAREN   
        self.RIGHTPAREN = pygame.K_RIGHTPAREN  
        self.ASTERISK   = pygame.K_ASTERISK    
        self.PLUS       = pygame.K_PLUS        
        self.COMMA      = pygame.K_COMMA       
        self.MINUS      = pygame.K_MINUS       
        self.PERIOD     = pygame.K_PERIOD      
        self.SLASH      = pygame.K_SLASH       
        self._0         = pygame.K_0           
        self._1         = pygame.K_1           
        self._2         = pygame.K_2           
        self._3         = pygame.K_3           
        self._4         = pygame.K_4           
        self._5         = pygame.K_5           
        self._6         = pygame.K_6           
        self._7         = pygame.K_7           
        self._8         = pygame.K_8           
        self._9         = pygame.K_9           
        self.COLON      = pygame.K_COLON       
        self.SEMICOLON  = pygame.K_SEMICOLON   
        self.LESS       = pygame.K_LESS        
        self.EQUALS     = pygame.K_EQUALS      
        self.GREATER    = pygame.K_GREATER     
        self.QUESTION   = pygame.K_QUESTION    
        self.AT         = pygame.K_AT          
        self.LEFTBRACKET= pygame.K_LEFTBRACKET 
        self.BACKSLASH  = pygame.K_BACKSLASH   
        self.RIGHTBRACKE= pygame.K_RIGHTBRACKET
        self.CARET      = pygame.K_CARET       
        self.UNDERSCORE = pygame.K_UNDERSCORE  
        self.BACKQUOTE  = pygame.K_BACKQUOTE   
        self.a          = pygame.K_a           
        self.b          = pygame.K_b           
        self.c          = pygame.K_c           
        self.d          = pygame.K_d           
        self.e          = pygame.K_e           
        self.f          = pygame.K_f           
        self.g          = pygame.K_g           
        self.h          = pygame.K_h           
        self.i          = pygame.K_i           
        self.j          = pygame.K_j           
        self.k          = pygame.K_k           
        self.l          = pygame.K_l           
        self.m          = pygame.K_m           
        self.n          = pygame.K_n           
        self.o          = pygame.K_o           
        self.p          = pygame.K_p           
        self.q          = pygame.K_q           
        self.r          = pygame.K_r           
        self.s          = pygame.K_s           
        self.t          = pygame.K_t           
        self.u          = pygame.K_u           
        self.v          = pygame.K_v           
        self.w          = pygame.K_w           
        self.x          = pygame.K_x           
        self.y          = pygame.K_y           
        self.z          = pygame.K_z           
        self.DELETE     = pygame.K_DELETE      
        self.KP0        = pygame.K_KP0         
        self.KP1        = pygame.K_KP1         
        self.KP2        = pygame.K_KP2         
        self.KP3        = pygame.K_KP3         
        self.KP4        = pygame.K_KP4         
        self.KP5        = pygame.K_KP5         
        self.KP6        = pygame.K_KP6         
        self.KP7        = pygame.K_KP7         
        self.KP8        = pygame.K_KP8         
        self.KP9        = pygame.K_KP9         
        self.KP_PERIOD  = pygame.K_KP_PERIOD   
        self.KP_DIVIDE  = pygame.K_KP_DIVIDE   
        self.KP_MULTIPLY= pygame.K_KP_MULTIPLY 
        self.KP_MINUS   = pygame.K_KP_MINUS    
        self.KP_PLUS    = pygame.K_KP_PLUS     
        self.KP_ENTER   = pygame.K_KP_ENTER    
        self.KP_EQUALS  = pygame.K_KP_EQUALS   
        self.UP         = pygame.K_UP          
        self.DOWN       = pygame.K_DOWN        
        self.RIGHT      = pygame.K_RIGHT       
        self.LEFT       = pygame.K_LEFT        
        self.INSERT     = pygame.K_INSERT      
        self.HOME       = pygame.K_HOME        
        self.END        = pygame.K_END         
        self.PAGEUP     = pygame.K_PAGEUP      
        self.PAGEDOWN   = pygame.K_PAGEDOWN    
        self.F1         = pygame.K_F1          
        self.F2         = pygame.K_F2          
        self.F3         = pygame.K_F3          
        self.F4         = pygame.K_F4          
        self.F5         = pygame.K_F5          
        self.F6         = pygame.K_F6          
        self.F7         = pygame.K_F7          
        self.F8         = pygame.K_F8          
        self.F9         = pygame.K_F9          
        self.F10        = pygame.K_F10         
        self.F11        = pygame.K_F11         
        self.F12        = pygame.K_F12         
        self.F13        = pygame.K_F13         
        self.F14        = pygame.K_F14         
        self.F15        = pygame.K_F15         
        self.NUMLOCK    = pygame.K_NUMLOCK     
        self.CAPSLOCK   = pygame.K_CAPSLOCK    
        self.SCROLLOCK  = pygame.K_SCROLLOCK   
        self.RSHIFT     = pygame.K_RSHIFT      
        self.LSHIFT     = pygame.K_LSHIFT      
        self.RCTRL      = pygame.K_RCTRL       
        self.LCTRL      = pygame.K_LCTRL       
        self.RALT       = pygame.K_RALT        
        self.LALT       = pygame.K_LALT        
        self.RMETA      = pygame.K_RMETA       
        self.LMETA      = pygame.K_LMETA       
        self.LSUPER     = pygame.K_LSUPER      
        self.RSUPER     = pygame.K_RSUPER      
        self.MODE       = pygame.K_MODE        
        self.HELP       = pygame.K_HELP        
        self.PRINT      = pygame.K_PRINT       
        self.SYSREQ     = pygame.K_SYSREQ      
        self.BREAK      = pygame.K_BREAK       
        self.MENU       = pygame.K_MENU        
        self.POWER      = pygame.K_POWER       
        self.EURO       = pygame.K_EURO        
        self.AC_BACK    = pygame.K_AC_BACK
        # Action list
        self.actions = []
    #
    # getHandler
    #
    def getHandler(self):
        dictionary = {
            key: lambda entity=entity, action=action, param=param: (
                getattr(entity, action)(param) if param is not None else getattr(entity, action)()
            )
            for key, entity, action, param in self.actions
        }
        return dictionary
    #
    # addHandler
    #
    def addHandler(self, key, entity, action, param=None):
        self.actions.append((key, entity, action, param))
    #
    # remHandler
    #
    def remHandler(self, key):
        if key in self.actions:
            del self.actions[key]