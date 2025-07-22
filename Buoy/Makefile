

SRCS := $(wildcard *.c) $(wildcard Sensors/*.c) $(wildcard UI/*.c)

OBJS := $(SRCS:.c=.o)

CC	:= gcc
CFLAGS   := -std=c11 -Wall -DHOST_BUILD -I../include

.PHONY: all
all: firmware_sim

firmware_sim: $(OBJS)
	$(CC) $(CFLAGS) -o firmware_sim $(OBJS)

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@

.PHONY: clean

clean:
	rm -f *.o firmware_sim

