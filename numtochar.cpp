/*
 http://weibo.com/1915548291/yCvGa7Ypj
 #谷歌面试题# 翻译数字串，类似于电话号码翻译：给一个数字串，比如12259，映射到字母数组，比如，1 -> a， 2-> b，... ， 12 -> l ，... 26-> z。那么，12259 -> lyi 或 abbei 或 lbei 或 abyi。输入一个数字串，判断是否能转换成字符串，如果能，则打印所以有可能的转换成的字符串。动手写写吧。
 */

#include <iostream>

/*
 dfs 即深度优先搜索
 return:所有可能的字符串总数
 num(in):数字串
 len(in):数字串长度
 s(out):存储转换的字符串，这个串的长度至少为原始数字串的长度+1
 sindex(in):准备存放下一个转换字符在s中的位置
 */
int dfs(char num[], int len, char s[], int sindex) {
  if (len <= 0) {
    s[sindex] = '\0';
    printf("%s\n", s);
    return 1;
  }
  if (num[0] == '0') {
    return 0;
  }
  int one = 0, two = 0;
  
  s[sindex] = num[0] - '0' + 'a' - 1;
  one = dfs(num + 1, len - 1, s, sindex + 1);
  
  if (len >= 2) {
    int v = (num[0] - '0') * 10 + num[1] - '0';
    if (v <= 26) {
      s[sindex] = v + 'a' - 1;
      two = dfs(num + 2, len - 2, s, sindex + 1);
    }
  }
  return one + two;
}

int main(int argc, const char * argv[])
{
  char s[1000] = {'\0'};
  
  char *num = "2222222";
  int r = dfs(num, strlen(num), s, 0);
  printf("r = %d\n", r);

  return 0;
}

