### Static Analyse ###
<br/>

**pylint** was used for anaylizing code parts. There are several warnings on files.<br/><br/>

Almost in every python file there missing proper **docstring warnings** were exist.
- (missing-module-docstring)
- (missing-class-docstring)
- (missing-function-docstring)

In some folders they were corrected. In general those warnings can be neglected.<br/><br/>

**snake_case naming style**<br/>
This warning were occured in most of the code snippets.
This rule of naming restricts of usages of one-letter variable names. That is why,
loop iteration variables, temporarily assigned variables in functions raise this warning 
message. Usually, in other languages like C++, Java this warning was not raised because, 
those languages are type-forced. Due to fact that project is library of algorithms, it is 
usual to use those tye of variables in most cases.<br/><br/>

**(too-few-public-methods)**
This warning can also be neglected for this project. Because it is more common warning for
object-oriented projects. As they are algorithmic functions in this project, no need for public
method limitions for this.<br/><br/>

**(useless-object-inheritance)**
There's two styles of classes depending on the presence or absence of object as a base-class.
- *classic style classes*: they don't have object as a base class
- *new style classes*: they have, directly or indirectly (e.g inherit from a built-in type), object as a base class

In Python 3, things are simplified. Only new-style classes exist (referred to plainly as classes). Wherever this warning
occured, it is because of inheritance from Object class.

<br/>

There are several other warnings those were corrected after discussing with teammates. There were whitespaces in the 
end of some files. Indentions those do not support clean code principles were occured while running static analyse were
also corrected. Some variable names those are not explanative itself were modified. In the some parts of project, there were 
unused local variables which were removed too.

<br/><br/>