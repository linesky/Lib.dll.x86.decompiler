
@color 40
@set paths=%PATH%
@set PATH=c:\mingw\bin\;c:\nasm\;%paths%
@objdump -M intel -d -h "%1"
@set PATH=%paths%