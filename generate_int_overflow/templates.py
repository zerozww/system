# sa-bAbI: An automated software assurance code dataset generator
# 
# Copyright 2018 Carnegie Mellon University. All Rights Reserved.
#
# NO WARRANTY. THIS CARNEGIE MELLON UNIVERSITY AND SOFTWARE
# ENGINEERING INSTITUTE MATERIAL IS FURNISHED ON AN "AS-IS" BASIS.
# CARNEGIE MELLON UNIVERSITY MAKES NO WARRANTIES OF ANY KIND, EITHER
# EXPRESSED OR IMPLIED, AS TO ANY MATTER INCLUDING, BUT NOT LIMITED
# TO, WARRANTY OF FITNESS FOR PURPOSE OR MERCHANTABILITY, EXCLUSIVITY,
# OR RESULTS OBTAINED FROM USE OF THE MATERIAL. CARNEGIE MELLON
# UNIVERSITY DOES NOT MAKE ANY WARRANTY OF ANY KIND WITH RESPECT TO
# FREEDOM FROM PATENT, TRADEMARK, OR COPYRIGHT INFRINGEMENT.
#
# Released under a MIT (SEI)-style license, please see license.txt or
# contact permission@sei.cmu.edu for full terms.
#
# [DISTRIBUTION STATEMENT A] This material has been approved for
# public release and unlimited distribution. Please see Copyright
# notice for non-US Government use and distribution.
# 
# Carnegie Mellon (R) and CERT (R) are registered in the U.S. Patent
# and Trademark Office by Carnegie Mellon University.
#
# This Software includes and/or makes use of the following Third-Party
# Software subject to its own license:
# 1. clang (http://llvm.org/docs/DeveloperPolicy.html#license)
#     Copyright 2018 University of Illinois at Urbana-Champaign.
# 2. frama-c (https://frama-c.com/download.html) Copyright 2018
#     frama-c team.
# 3. Docker (https://www.apache.org/licenses/LICENSE-2.0.html)
#     Copyright 2004 Apache Software Foundation.
# 4. cppcheck (http://cppcheck.sourceforge.net/) Copyright 2018
#     cppcheck team.
# 5. Python 3.6 (https://docs.python.org/3/license.html) Copyright
#     2018 Python Software Foundation.
# 
# DM18-0995
# 
"""templates.py: Templates for SA-bAbI code generation"""

# BUFWRITE_LINES = ["$buf_var[$idx_var] = '$char';"]

# templates for functions without free variables

INTCALCFLOW_ADD = [
    "$int_var += $overflow_var;"
]

INTCALCFLOW_MINUS = [
    "$int_var -= $overflow_var;"
]

INTCALCFLOW_MULTI = [
    "$int_var *= $overflow_var;"
]

COND_DEC_INIT_PAIRS = [
    ("int $overflow_var;", None),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $thresh_var;", "$thresh_var = $thresh;")
]
COND_MAIN_LINES_ADD = [
    "if($int_var > $thresh_var){",
    "$overflow_var = $true_int;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_MAIN_LINES_MINUS = [
    "if( -$int_var < $thresh_var){",
    "$overflow_var = $true_int;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_MAIN_LINES_LOWER = [
    "if($int_var < $thresh_var){",
    "$overflow_var = $true_int;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
WHILE_DEC_INIT_PAIRS = [
    ("int $overflow_var;", "$overflow_var = 0;"),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $count_var;", "$count_var = $count_int;")
]
WHILE_DEC_INIT_PAIRS_LOWER = [
    ("int $overflow_var;", "$overflow_var = $overflow_int;"),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $count_var;", "$count_var = $count_int;")
]
WHILE_MAIN_LINES_ADD = [
    "int i = 0;",
    "while(i < $count_var){",
    "$overflow_var += 1000000;",
    "i++;",
    "}"
]
WHILE_MAIN_LINES_MINUS = [
    "int i = 0;",
    "while(i < $count_var){",
    "$overflow_var -= 1000000;",
    "i++;",
    "}"
]
WHILE_MAIN_LINES_MULTI = [
    "if($count_var > 0){",
    "$overflow_var = 1;",
    "while($overflow_var < $count_var){",
    "$overflow_var *= 2;",
    "if($overflow_var * 2 > $count_var){",
    "$overflow_var = $count_var;",
    "break;",
    "}",
    "}",
    "}else{",
    "$overflow_var = -1;",
    "while($overflow_var > $count_var){",
    "$overflow_var *= 2;",
    "if($overflow_var * 2 < $count_var){",
    "$overflow_var = $count_var;",
    "break;",
    "}",
    "}"
    "}",
]
WHILE_MAIN_LINES_ADD_HIGHER = [
    "int i = 0;",
    "while(i > $count_var){",
    "$overflow_var += -1000000;",
    "i--;",
    "}"
]
WHILE_MAIN_LINES_MINUS_HIGHER = [
    "int i = 0;",
    "while(i > $count_var){",
    "$overflow_var -= -1000000;",
    "i--;",
    "}"
]
FOR_DEC_INIT_PAIRS = [
    ("int $overflow_var;", "$overflow_var = 0;"),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $count_var;", "$count_var = $count_int;")
]
FOR_DEC_INIT_PAIRS_LOWER = [
    ("int $overflow_var;", "$overflow_var = $overflow_int;"),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $count_var;", "$count_var = $count_int;")
]
FOR_MAIN_LINES_ADD = [
    "for(int i = 0; i < $count_var; i++){",
    "$overflow_var += 1000000;",
    "}"
]
FOR_MAIN_LINES_MINUS = [
    "for(int i = 0; i < $count_var; i++){",
    "$overflow_var -= 1000000;",
    "}"
]
FOR_MAIN_LINES_MULTI = [
    "if($count_var > 0){",
    "for($overflow_var = 1; $overflow_var < $count_var; $overflow_var *= 2){",
    "if($overflow_var * 2 > $count_var){",
    "$overflow_var = $count_var;",
    "break;",
    "}"
    "}",
    "}else{",
    "for($overflow_var = -1; $overflow_var > $count_var; $overflow_var *= 2){",
    "if($overflow_var * 2 < $count_var){",
    "$overflow_var = $count_var;",
    "break;",
    "}",
    "}"
    "}",
]
FOR_MAIN_LINES_ADD_HIGHER = [
    "for(int i = 0; i > $count_var; i--){",
    "$overflow_var += -1000000;",
    "}"
]
FOR_MAIN_LINES_MINUS_HIGHER = [
    "for(int i = 0; i > $count_var; i--){",
    "$overflow_var -= -1000000;",
    "}"
]
# templates for functions with one free variable

COND_FV_DEC_INIT_PAIRS = [
    ("int $free_var;", "$free_var = rand();"),
    ("int $overflow_var;", None),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $thresh_var;", "$thresh_var = $thresh_int;")
]
COND_FV_MAIN_LINES_ADD = [
    "if($free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_FV_MAIN_LINES_MINUS = [
    "if( -$free_var > $thresh_var){",
    "$overflow_var = -$free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_FV_MAIN_LINES_MULTI = [
    "$free_var %= 53970;",
    "if($free_var < $thresh_var || -$free_var > $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_FV_MAIN_LINES_ADD_LOWER = [
    "if($free_var > $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_FV_MAIN_LINES_MINUS_LOWER = [
    "if( $free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_FV_MAIN_LINES_ADD_HIGHER = [
    "if($free_var > $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]
COND_FV_MAIN_LINES_MINUS_HIGHER = [
    "if( $free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}"
]

WHILE_FV_DEC_INIT_PAIRS = [
    ("int $overflow_var;", None),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $thresh_var;", "$thresh_var = $thresh_int;"),
    ("int $free_var;", "$free_var = rand();")
]
WHILE_FV_DEC_INIT_PAIRS_LOWER = [
    ("int $overflow_var;", "$overflow_var=$overflow_int;"),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $thresh_var;", "$thresh_var = $thresh_int;"),
    ("int $free_var;", "$free_var = rand();"),
    ("int $count_var;",None)
]
WHILE_FV_MAIN_LINES_ADD = [
    "if ($free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int i = 0;",
    "int $count_var = $overflow_var / 1000000;",
    "$overflow_var = 0;",
    "while(i < $count_var){",
    "$overflow_var += 1000000;",
    "i++;",
    "}"
]
WHILE_FV_MAIN_LINES_MINUS = [
    "if ( -$free_var > $thresh_var){",
    "$overflow_var = -$free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int i = 0;",
    "int $count_var = $overflow_var / -1000000;",
    "$overflow_var = 0;",
    "while(i < $count_var){",
    "$overflow_var -= 1000000;",
    "i++;",
    "}"
]
WHILE_FV_MAIN_LINES_MULTI = [
    "if ($free_var < $thresh_var || -$free_var > $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "if($overflow_var < 0){",
    "$overflow_var = - $overflow_var;"
    "}",
    "int i = 0;",
    "int $count_var = 0;",
    "while(($overflow_var / 2) >= 2){",
    "$count_var++;",
    "$overflow_var = $overflow_var / 2;",
    "}",
    "$overflow_var = 1;",
    "while(i < $count_var){",
    "$overflow_var *= 2;",
    "i++;",
    "}"
]
WHILE_FV_MAIN_LINES_ADD_LOWER = [
    "if ($free_var < $thresh_var){",
    "$count_var = $free_var;",
    "} else {",
    "$count_var = $false_int;",
    "}",
    "int i = 0;",
    "while(i < $count_var){",
    "$overflow_var += 1000000;",
    "i++;",
    "}"
]
# WHILE_FV_DEC_INIT_PAIRS_LOWER = [
#     ("int $overflow_var;", None),
#     ("int $int_var;", "$int_var = $int_init;"),
#     ("int $thresh_var;", "$thresh_var = $thresh_int;"),
#     ("int $free_var;", "$free_var = rand();"),
#     ("int $count_var", "$count_var = $count_int;")
# ]
WHILE_FV_MAIN_LINES_ADD_HIGHER = [
    "if ($free_var > $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int i = 0;",
    "int $count_var = $overflow_var / 1000000;",
    "$overflow_var = 0;",
    "while(i > $count_var){",
    "$overflow_var += -1000000;",
    "i--;",
    "}"
]
WHILE_FV_MAIN_LINES_ADD_LOWER = [
    "if ($free_var > $thresh_var){",
    "$count_var = $free_var;",
    "} else {",
    "$count_var = $false_int;",
    "}",
    "int i = 0;",
    "while(i > $count_var){",
    "$overflow_var += -1000000;",
    "i--;",
    "}"
]
WHILE_FV_MAIN_LINES_MINUS_LOWER = [
    "if ($free_var < $thresh_var){",
    "$count_var = $free_var;",
    "} else {",
    "$count_var = $false_int;",
    "}",
    "int i = 0;",
    "while(i < $count_var){",
    "$overflow_var -= 1000000;",
    "i++;",
    "}"
]
WHILE_FV_MAIN_LINES_MINUS_LOWER = [
    "if ($free_var < $thresh_var){",
    "$count_var = $free_var;",
    "} else {",
    "$count_var = $false_int;",
    "}",
    "int i = 0;",
    "while(i < $count_var){",
    "$overflow_var -= 1000000;",
    "i++;",
    "}"
]
WHILE_FV_MAIN_LINES_MINUS_HIGHER = [
    "if ( $free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int i = 0;",
    "int $count_var = $overflow_var / 1000000;",
    "$overflow_var = 0;",
    "while(i < $count_var){",
    "$overflow_var -= -1000000;",
    "i++;",
    "}"
]

FOR_FV_DEC_INIT_PAIRS = [
    ("int $overflow_var;", None),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $thresh_var;", "$thresh_var = $thresh_int;"),
    ("int $free_var;", "$free_var = rand();")
]
FOR_FV_DEC_INIT_PAIRS_LOWER = [
    ("int $overflow_var;", "$overflow_var=$overflow_int;"),
    ("int $int_var;", "$int_var = $int_init;"),
    ("int $thresh_var;", "$thresh_var = $thresh_int;"),
    ("int $free_var;", "$free_var = rand();"),
    ("int $count_var;", None)
]
FOR_FV_MAIN_LINES_ADD_HIGHER = [
    "if ($free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int $count_var = $overflow_var / 1000000;",
    "$overflow_var = 0;",
    "for(int i = 0; i > $count_var; i--){",
    "$overflow_var += -1000000;",
    "}"
]
FOR_FV_MAIN_LINES_ADD_LOWER = [
    "if ($free_var < $thresh_var){",
    "$count_var = $free_var;",
    "} else {",
    "$count_var = $false_int;",
    "}",
    "for(int i = 0; i < $count_var; i++)",
    "$overflow_var += 1000000;",
    "}"
]
FOR_FV_MAIN_LINES_ADD = [
    "if ($free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int $count_var = $overflow_var / 1000000;",
    "$overflow_var = 0;",
    "for(int i = 0; i < $count_var; i++){",
    "$overflow_var += 1000000;",
    "}"
]
FOR_FV_MAIN_LINES_MINUS = [
    "if (-$free_var > $thresh_var){",
    "$overflow_var = -$free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int $count_var = $overflow_var / -1000000;",
    "$overflow_var = 0;",
    "for(int i = 0; i < $count_var; i++){",
    "$overflow_var -= 1000000;",
    "}"
]
FOR_FV_MAIN_LINES_MINUS_HIGHER = [
    "if ($free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "int $count_var = $overflow_var / 1000000;",
    "$overflow_var = 0;",
    "for(int i = 0; i > $count_var; i--){",
    "$overflow_var -= -1000000;",
    "}"
]
FOR_FV_MAIN_LINES_MINUS_LOWER = [
    "if ($free_var < $thresh_var){",
    "$count_var = $free_var;",
    "} else {",
    "$count_var = $false_int;",
    "}",
    "for(int i = 0; i < $count_var; i++)",
    "$overflow_var -= 1000000;",
]
FOR_FV_MAIN_LINES_MULTI = [
    "$free_var %= 53970;",
    "if ($free_var < $thresh_var){",
    "$overflow_var = $free_var;",
    "} else {",
    "$overflow_var = $false_int;",
    "}",
    "if($overflow_var < 0)",
    "$overflow_var = - $overflow_var;",
    "int $count_var = 0;",
    "while(($overflow_var / 2) >= 2){",
    "$count_var++;",
    "$overflow_var = $overflow_var / 2;",
    "}",
    "$overflow_var = 1;",
    "for(int i = 0; i < $count_var; i++){",
    "$overflow_var = $overflow_var * 2;",
    "}"
]

# main function body wrapper

FUNC_TMPL_STR = """#include <stdlib.h>
int main()
{
$body
    return 0;
}"""
