BIN_PATH = ../register-computer/kerberos/bin/

default: dist

clean:
	rm -f ksetpwd.o ksetpwd

ksetpwd.o:
	gcc -DHAVE_CONFIG_H -DKRB5_DEPRECATED=1 -DKRB5_PRIVATE  -g -O2 -Wall -Wcast-align -Wshadow -Wmissing-prototypes -Wno-format-zero-length -Woverflow -Wstrict-overflow -Wmissing-format-attribute -Wmissing-prototypes -Wreturn-type -Wmissing-braces -Wparentheses -Wswitch -Wunused-function -Wunused-label -Wunused-variable -Wunused-value -Wunknown-pragmas -Wsign-compare -Werror=uninitialized -Wno-maybe-uninitialized -Werror=pointer-arith -Werror=int-conversion -Werror=incompatible-pointer-types -Werror=discarded-qualifiers -Werror=implicit-int -Werror=declaration-after-statement -Werror-implicit-function-declaration -pthread  -c ksetpwd.c

ksetpwd: ksetpwd.o
	gcc -Wl,--enable-new-dtags -Wl,-rpath -Wl,/usr/local/lib -g -O2   -o ksetpwd ksetpwd.o -lkrb5 -lk5crypto -lcom_err -lkrb5support  -lresolv  -ldl

dist: ksetpwd
	mkdir -p $(BIN_PATH)
	cp ksetpwd $(BIN_PATH)
	cp /lib/x86_64-linux-gnu/libcom_err.* $(BIN_PATH)
