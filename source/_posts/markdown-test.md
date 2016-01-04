title: Markdown Test
date: 2009-04-20
tags:
- misc
---

Markdown demo/test.

<!-- more -->

{% blockquote %}
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque hendrerit lacus ut purus iaculis feugiat. Sed nec tempor elit, quis aliquam neque. Curabitur sed diam eget dolor fermentum semper at eu lorem.
{% endblockquote %}

{% blockquote David Levithan, Wide Awake %}
Do not just seek happiness for yourself. Seek happiness for all. Through kindness. Through mercy.
{% endblockquote %}

{% blockquote @DevDocs https://twitter.com/devdocs/status/356095192085962752 %}
NEW: DevDocs now comes with syntax highlighting. http://devdocs.io
{% endblockquote %}

{% blockquote Seth Godin http://sethgodin.typepad.com/seths_blog/2009/07/welcome-to-island-marketing.html Welcome to Island Marketing %}
Every interaction is both precious and an opportunity to delight.
{% endblockquote %}

{% codeblock lang:c %}
#include <stdio.h>
#include <string.h>
void reverse_char_array(char * first, char * last) {
    while (first != last && first != --last) {
        *first ^= *last;
        *last ^= *first;
        *first++ ^= *last;
    }
}
void reverse_string(char * sentence) {
    reverse_char_array(sentence, &sentence[strlen(sentence)]);
}
void reverse_word(char * sentence) {
    char * end_s = &sentence[strlen(sentence)], * end_w;
    while (end_w != end_s) {
        if (!(end_w = strchr(sentence, ' '))) end_w = end_s;
        reverse_char_array(sentence, end_w);
        sentence = end_w + 1;
    }
}
int main(int argc, char ** argv) {
    char sentence[] = "how are you";
    reverse_string(sentence);
    reverse_word(sentence);
    printf("%s\n", sentence);
    return 0;
}
{% endcodeblock %}

``` py
#!/usr/bin/env python
# -*- coding: utf-8 -*-
import Queue
import argparse
import os
import random
import subprocess
import sys
import threading
import time

class Tester(threading.Thread):
    def __init__(self, testee, answer_queue, counter_queue):
        threading.Thread.__init__(self)
        self.testee = testee
        self.answer_queue = answer_queue
        self.counter_queue = counter_queue
    def run(self):
        while True:
            ans = self.answer_queue.get()
            counter = 1
            p = subprocess.Popen(self.testee,
                    stdin=subprocess.PIPE, stdout=subprocess.PIPE)
            while True:
                guess = p.stdout.readline().strip()
                bulls = sum(1 for i, j in zip(ans, guess) if i == j)
                cows = sum(1 for i, j in zip(ans, guess)if i != j and j in ans)
                score = str(bulls) + 'a' + str(cows) + 'b' + '\n'
                p.stdin.write(score)
                if bulls == 4:
                    self.answer_queue.task_done()
                    self.counter_queue.put(counter)
                    counter = 1
                    break
                counter += 1
            if self.answer_queue.empty():
                break

def get_args():
    args_parser = argparse.ArgumentParser(
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Profile a bulls-and-cows guesser.',
            epilog='EXAMPLE:\n' \
                    "  {} -j 8 './bulls-and-cows-guesser.py'".format(os.path.basename(__file__))
                    )
    args_parser.add_argument('testee' , metavar='TESTEE',
            help='the guesser you want to evaluate')
    args_parser.add_argument('-j', '--jobs', metavar='N', type=int, default=1,
            help='allow N jobs at once')
    args_parser.add_argument('--no-shuffle', action='store_true',
            help='do not shuffle the test casees')
    return args_parser.parse_args()

def get_all_answers(shuffle):
    answer_candidates = [str(i) + str(j) + str(k) + str(l) \
                for i in xrange(0, 10) for j in xrange(0, 10) \
                for k in xrange(0, 10) for l in xrange(0, 10) \
                if len(set(str(i) + str(j) + str(k) + str(l))) == 4]

    if shuffle:
        random.shuffle(answer_candidates)

    return answer_candidates

def main():
    args = get_args()
    answer_candidates = get_all_answers(not args.no_shuffle)

    answer_queue = Queue.Queue()
    counter_queue = Queue.Queue()
    for ans in answer_candidates:
        answer_queue.put(ans)
    for i in xrange(args.jobs):
        t = Tester(args.testee, answer_queue, counter_queue)
        t.daemon = True
        t.start()

    answer_queue.join()
    while True:
        if counter_queue.qsize() == len(answer_candidates):
            break

    counter = []
    for i in xrange(len(answer_candidates)):
        counter.append(counter_queue.get())

    print 'avg: ', float(sum(counter)) / len(counter)
    d = {}
    for v in counter:
        if v not in d:
            d[v] = 1
            continue
        d[v] += 1
    print str(d)[1:len(str(d))-1]

if __name__ == '__main__':
    main()

```

{% codeblock .compact http://underscorejs.org/#compact Underscore.js %}
.compact([0, 1, false, 2, ‘’, 3]);
=> [1, 2, 3]
{% endcodeblock %}

{% gist 9265765 %}

$a = b + c$
$A = B + C$

$$\frac{\partial u}{\partial t}
= h^2 \left( \frac{\partial^2 u}{\partial x^2} +
\frac{\partial^2 u}{\partial y^2} +
\frac{\partial^2 u}{\partial z^2}\right)$$

This equation {% math %} \cos 2\theta = \cos^2 \theta - \sin^2 \theta =  2 \cos^2 \theta - 1 {% endmath %} is inline.

{% math %}
\begin{aligned}
\dot{x} & = \sigma(y-x) \\
\dot{y} & = \rho x - y - xz \\
\dot{z} & = -\beta z + xy
\end{aligned}
{% endmath %}

| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ | :-------------: | ------------: |
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |

| Left-Aligned  | Center Aligned  | Right Aligned |
| :------------ | :-------------- | :------------ |
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |

| Left-Aligned  | Center Aligned  | Right Aligned | Left-Aligned  | Center Aligned  | Right Aligned | Left-Aligned  | Center Aligned  | Right Aligned | Left-Aligned  | Center Aligned  | Right Aligned |
| :-----------: | :-------------: | :-----------: | :-----------: | :-------------: | :-----------: | :-----------: | :-------------: | :-----------: | :-----------: | :-------------: | :-----------: |
| col 3 is      | some wordy text |         $1600 | col 3 is      | some wordy text |         $1600 | col 3 is      | some wordy text |         $1600 | col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 | col 2 is      | centered        |           $12 | col 2 is      | centered        |           $12 | col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 | zebra stripes | are neat        |            $1 | zebra stripes | are neat        |            $1 | zebra stripes | are neat        |            $1 |

| Left-Aligned  | Center Aligned  | Right Aligned |
| ------------: | --------------: | ------------: |
| col 3 is      | some wordy text |         $1600 |
| col 2 is      | centered        |           $12 |
| zebra stripes | are neat        |            $1 |

perform_complicated_task
do_this_and_do_that_and_another_thing

http://example.com

~~deleted.~~

{% raw %}
content<br />
1. a<br />
1. b<br />
    1. A<br />
    1. B<br />
    * C<br />
ABCDEFG<br />
1234567<br />
{% endraw %}

![](超級賽亞羊.jpg)
![](github-commit-amount-cheat.png)

{% asset_img 超級賽亞羊.jpg [小六畫的] %}
{% asset_img github-commit-amount-cheat.png %}

{% jsfiddle 69z2wepo %}
