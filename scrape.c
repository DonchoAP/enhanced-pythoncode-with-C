#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/*gcc scrape_text.c -o scrape_text*/

int main(int argc, char *argv[]) {
    if (argc != 3) {
        printf("Usage: %s <url> <output_filename>\n", argv[0]);
        return 1;
    }

    char command[1000];
    sprintf(command, "curl %s | grep -oE '\\b\\w+\\b' > %s", argv[1], argv[2]);
    system(command);

    return 0;
}