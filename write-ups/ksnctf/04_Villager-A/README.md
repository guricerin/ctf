```bash
$ ssh q4@ctfq.u1tramarine.blue -p 10004

[q4@eceec62b961b ~]$ ls -alF
total 32
dr-xr-xr-x 1 root root 4096 Feb 27  2021 ./
drwxr-xr-x 1 root root 4096 Feb 27  2021 ../
-rw-r--r-- 1 root root   18 Jul 21  2020 .bash_logout
-rw-r--r-- 1 root root  141 Jul 21  2020 .bash_profile
-rw-r--r-- 1 root root  456 Feb 27  2021 .bashrc
-r--r----- 1 root q4a    22 Feb 26  2021 flag.txt
-r-xr-sr-x 1 root q4a  5857 Feb 26  2021 q4*
```

``flag.txt``は権限がないので覗けない。  

謎の実行ファイルがあるので動かしてみる。  

```bash
$ ./q4
What's your name?
q4a
Hi, q4a

Do you want the flag?
yes
Do you want the flag?
Y
Do you want the flag?
N
Do you want the flag?
aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
Do you want the flag?
n
Do you want the flag?
no
I see. Good bye.
```

わけわからん。  

```bash
$ strings q4 | less
```

```
/lib/ld-linux.so.2
libstdc++.so.6
__gmon_start__
_Jv_RegisterClasses
__gxx_personality_v0
libm.so.6
libgcc_s.so.1
libc.so.6
_IO_stdin_used
fopen
puts
putchar
stdin
printf
fgets
strcmp
__libc_start_main
CXXABI_1.3
GLIBC_2.1
GLIBC_2.0
PTRh
[^_]
What's your name?
Hi,
Do you want the flag?
I see. Good bye.
flag.txt
GCC: (GNU) 4.4.6 20110731 (Red Hat 4.4.6-3)
.symtab
.strtab
.shstrtab
.interp
.note.ABI-tag
.note.gnu.build-id
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rel.dyn
.rel.plt
.init
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.ctors
.dtors
.jcr
.dynamic
.got
.got.plt
.data
.bss
.comment
crtstuff.c
__CTOR_LIST__
__DTOR_LIST__
__JCR_LIST__
__do_global_dtors_aux
completed.5972
dtor_idx.5974
frame_dummy
__CTOR_END__
__FRAME_END__
__JCR_END__
__do_global_ctors_aux
q4.cpp
_GLOBAL_OFFSET_TABLE_
__init_array_end
__init_array_start
_DYNAMIC
data_start
__libc_csu_fini
_start
__gmon_start__
_Jv_RegisterClasses
_fp_hw
_fini
putchar@@GLIBC_2.0
fgets@@GLIBC_2.0
__libc_start_main@@GLIBC_2.0
_IO_stdin_used
__data_start
fopen@@GLIBC_2.1
__dso_handle
__DTOR_END__
__libc_csu_init
printf@@GLIBC_2.0
__bss_start
stdin@@GLIBC_2.0
_end
puts@@GLIBC_2.0
_edata
__gxx_personality_v0@@CXXABI_1.3
strcmp@@GLIBC_2.0
__i686.get_pc_thunk.bx
main
_init
```

``flag.txt``は読み込むようだ。読み込ませる条件はさっぱりわからんが。  

``scp``でローカルに送ってみる。  

```bash
$ scp -P 10004 q4@ctfq.u1tramarine.blue:~/q4 .
q4@ctfq.u1tramarine.blue's password:
bash: scp: command not found
```

そうかい。  

仕方ない。``gdb``を使う。  

```bash
$ gdb ./q4
GNU gdb (GDB) Red Hat Enterprise Linux 8.2-12.el8
Copyright (C) 2018 Free Software Foundation, Inc.
License GPLv3+: GNU GPL version 3 or later <http://gnu.org/licenses/gpl.html>
This is free software: you are free to change and redistribute it.
There is NO WARRANTY, to the extent permitted by law.
Type "show copying" and "show warranty" for details.
This GDB was configured as "x86_64-redhat-linux-gnu".
Type "show configuration" for configuration details.
For bug reporting instructions, please see:
<http://www.gnu.org/software/gdb/bugs/>.
Find the GDB manual and other documentation resources online at:
    <http://www.gnu.org/software/gdb/documentation/>.

For help, type "help".
Type "apropos word" to search for commands related to "word"...
Reading symbols from ./q4...(no debugging symbols found)...done.
(gdb) b main
Breakpoint 1 at 0x80485b7
(gdb) disass
No frame selected.
(gdb) r
Starting program: /home/q4/q4
warning: Error disabling address space randomization: Operation not permitted
Missing separate debuginfos, use: yum debuginfo-install glibc-2.28-127.el8.i686
warning: Loadable section ".note.gnu.property" outside of ELF segments
warning: Loadable section ".note.gnu.property" outside of ELF segments

Breakpoint 1, 0x080485b7 in main ()
Missing separate debuginfos, use: yum debuginfo-install libgcc-8.3.1-5.1.el8.i686 libstdc++-8.3.1-5.1.el8.i686
```

```
(gdb) disass
Dump of assembler code for function main:
   0x080485b4 <+0>:     push   %ebp
   0x080485b5 <+1>:     mov    %esp,%ebp
=> 0x080485b7 <+3>:     and    $0xfffffff0,%esp
   0x080485ba <+6>:     sub    $0x420,%esp
   0x080485c0 <+12>:    movl   $0x80487a4,(%esp)
   0x080485c7 <+19>:    call   0x80484c4 <puts@plt> ; What's your name?
   0x080485cc <+24>:    mov    0x8049a04,%eax
   0x080485d1 <+29>:    mov    %eax,0x8(%esp)
   0x080485d5 <+33>:    movl   $0x400,0x4(%esp)
   0x080485dd <+41>:    lea    0x18(%esp),%eax
   0x080485e1 <+45>:    mov    %eax,(%esp)
   0x080485e4 <+48>:    call   0x8048484 <fgets@plt> ; 入力
   0x080485e9 <+53>:    movl   $0x80487b6,(%esp)
   0x080485f0 <+60>:    call   0x80484b4 <printf@plt> ; Hi, <name>
   0x080485f5 <+65>:    lea    0x18(%esp),%eax
   0x080485f9 <+69>:    mov    %eax,(%esp)
   0x080485fc <+72>:    call   0x80484b4 <printf@plt> ; Do you want the flag?
   0x08048601 <+77>:    movl   $0xa,(%esp)
   0x08048608 <+84>:    call   0x8048474 <putchar@plt> ; 改行。たぶん。
   0x0804860d <+89>:    movl   $0x1,0x418(%esp)
   0x08048618 <+100>:   jmp    0x8048681 <main+205>
   0x0804861a <+102>:   movl   $0x80487bb,(%esp)
   0x08048621 <+109>:   call   0x80484c4 <puts@plt>
   0x08048626 <+114>:   mov    0x8049a04,%eax
   0x0804862b <+119>:   mov    %eax,0x8(%esp)
   0x0804862f <+123>:   movl   $0x400,0x4(%esp)
   0x0804863b <+135>:   mov    %eax,(%esp)
   0x0804863e <+138>:   call   0x8048484 <fgets@plt>
   0x08048643 <+143>:   test   %eax,%eax
   0x08048645 <+145>:   sete   %al
   0x08048648 <+148>:   test   %al,%al
   0x0804864a <+150>:   je     0x8048656 <main+162>
   0x0804864c <+152>:   mov    $0x0,%eax
   0x08048651 <+157>:   jmp    0x80486dc <main+296>
   0x08048656 <+162>:   movl   $0x80487d1,0x4(%esp)
   0x0804865e <+170>:   lea    0x18(%esp),%eax
   0x08048662 <+174>:   mov    %eax,(%esp)
   0x08048665 <+177>:   call   0x80484e4 <strcmp@plt>
   0x0804866a <+182>:   test   %eax,%eax
   0x0804866c <+184>:   jne    0x8048681 <main+205>
   0x0804866e <+186>:   movl   $0x80487d5,(%esp)
   0x08048675 <+193>:   call   0x80484c4 <puts@plt>
   0x0804867a <+198>:   mov    $0x0,%eax
   0x0804867f <+203>:   jmp    0x80486dc <main+296>
   0x08048681 <+205>:   mov    0x418(%esp),%eax
   0x08048688 <+212>:   test   %eax,%eax
   0x0804868a <+214>:   setne  %al
   0x0804868d <+217>:   test   %al,%al
   0x0804868f <+219>:   jne    0x804861a <main+102>
   0x08048691 <+221>:   movl   $0x80487e6,0x4(%esp)
   0x08048699 <+229>:   movl   $0x80487e8,(%esp)
   0x080486a0 <+236>:   call   0x80484a4 <fopen@plt> ; flag.txtを読み込む？
   0x080486a5 <+241>:   mov    %eax,0x41c(%esp)
   0x080486ac <+248>:   mov    0x41c(%esp),%eax
   0x080486b3 <+255>:   mov    %eax,0x8(%esp)
   0x080486b7 <+259>:   movl   $0x400,0x4(%esp)
   0x080486bf <+267>:   lea    0x18(%esp),%eax
   0x080486c3 <+271>:   mov    %eax,(%esp)
   0x080486c6 <+274>:   call   0x8048484 <fgets@plt>
   0x080486cb <+279>:   lea    0x18(%esp),%eax
   0x080486cf <+283>:   mov    %eax,(%esp)
   0x080486d2 <+286>:   call   0x80484b4 <printf@plt> ; I see. Good bye.
   0x080486d7 <+291>:   mov    $0x0,%eax
   0x080486dc <+296>:   leave
   0x080486dd <+297>:   ret
End of assembler dump.
```
