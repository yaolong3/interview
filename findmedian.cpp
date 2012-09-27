//
//  findmedian.cpp
//  findmedian
//
//  Created by yaolong3 on 12-9-26.
//  Copyright (c) 2012年 yaolong3. All rights reserved.
//http://weibo.com/yaolong3

/*
 http://weibo.com/1915548291/yDCVICDOo
 #谷歌面试题# 两个sorted array，A和B，找其中值。证明复杂度。
 */

/*
 第一次提交的代码错了，现修正
 主要是对m<=2||n<=2的情况都考虑全
 期待同学们有更优雅和清晰的代码
 */
#include <iostream>
#include <algorithm>
#include <stdlib.h>

using namespace std;

double median(int A[], int m) {
  return (A[(m - 1) / 2] + A[m / 2]) / 2.0;
}

double FindMedianSortedArrays2(int A[], int m, int B[], int n);
void printArray(int A[], int m);

double FindMedianHelper2(int A[], int m, int B[], int n, int mm, int nn) {
//  static int s_cnt = 0;
//  ++s_cnt;
//  printf("s_cnt:%d\n", s_cnt);
  if (m <= 2 || n <= 2) {
    if (m == 0) {
      return median(B, n);
    } else if (n == 0) {
      return median(A, m);
    } else if (m == 1 && n == 1) {
      return (A[0] + B[0]) / 2.0;
    } else if (m == 1) {
      if (A[0] > B[(n - 1) / 2]) {
        return A[0];
      } else {
        if (n % 2) {
          if (A[0] <= B[n / 2 - 1]) {
            return (B[n / 2 - 1] + B[n / 2]) / 2.0;
          } else {
            return (A[0] + B[n / 2]) / 2.0;
          }
        } else {
          return B[(n - 1) / 2];
        }
      }
    } else if (n == 1) {
      if (B[0] < A[m / 2]) {
        return B[0];
      } else {
        if (m % 2) {
          if (B[0] <= A[m / 2 + 1]) {
            return (A[m / 2] + B[0]) / 2.0;
          } else {
            return (A[m / 2 + 1] + A[m / 2]) / 2.0;
          }
        } else {
          return A[m / 2];
        }
      }
    } else if (m == 2) {
      if (A[0] <= B[(n - 1) / 2]) {
        if (A[1] > B[n / 2]) {
          return median(B, n);
        }
      } else {
        return median(A, m);
      }
    } else if (n == 2) {
      if (B[0] <= A[(m - 1) / 2]) {
        return median(A, m);
      } else {
        if (B[1] < A[m / 2]) {
          return median(B, n);
        }
      }
    }
  }
  int kk = max(1, min(mm, n - nn - 1));
//  printArray(A, m);
//  printArray(B, n);
//  printf("kk = %d, m = %d, n = %d, mm = %d, nn = %d\n", kk, m, n, mm, nn);
  return FindMedianSortedArrays2(A + kk, m - kk, B, n - kk);
};

double FindMedianSortedArrays2(int A[], int m, int B[], int n) {
  double am = median(A, m);
  double bm = median(B, n);
  if (am < bm) {
    return FindMedianHelper2(A, m, B, n, (m - 1) / 2, n / 2);
  } else if (am > bm) {
    return FindMedianHelper2(B, n, A, m, (n - 1) / 2, m / 2);
  } else {
    return am;
  }
};

int *randomSortedArray(int m) {
  int *A = (int *)malloc(m * sizeof(int));
  A[0] = rand() % 50;
  for (int i = 1; i < m; ++i) {
    A[i] = A[i - 1] + rand() % 10;
  }
  return A;
}

void printArray(int A[], int m) {
  printf("[");
  for (int i = 0; i < m; ++i) {
    printf("%d ", A[i]);
  }
  printf("]");
  printf("count:%d\n", m);
}
//
double verify(int A[], int m, int B[], int n) {
  int *C = (int *)malloc((m + n) * sizeof(int));
  memcpy(C, A, m * sizeof(int));
  memcpy(C + m, B, n * sizeof(int));
  sort(C, C + m + n);
  double r = median(C, m + n);
  free(C);
  return r;
}

/////////////////////////////////////////////////////////////////////////////
void test(int times, int bound) {
  int err_cnt = 0;
  for (int i = 0; i < times; ++i) {
    int lenA = rand() % bound + 1;
    int lenB = rand() % bound + 1;
    int *A = randomSortedArray(lenA);
    int *B = randomSortedArray(lenB);
    double result = FindMedianSortedArrays2(A, lenA, B, lenB);
    double v = verify(A, lenA, B, lenB);
    if (v != result) {
      printf("error:%d %d  result:%lf v:%lf\n", lenA, lenB, result, v);
      printArray(A, lenA);
      printArray(B, lenB);
      ++err_cnt;
    } else {
      printf("right:%d %d  result:%lf v:%lf\n", lenA, lenB, result, v);
    }
    free(A);
    free(B);
  }
  printf("err_cnt / all : %d / %d\n", err_cnt, times);
}

int main(int argc, const char * argv[])
{
  srand((unsigned)time(NULL));
  double result;

  int lenA = 10;
  int lenB = 10;
  int *A = randomSortedArray(lenA);
  int *B = randomSortedArray(lenB);

  result = FindMedianSortedArrays2(A, lenA, B, lenB);
  
  printf("----------\n");
  printArray(A, lenA);
  printArray(B, lenB);
  printf("%lf\n", result);
  printf("right answer:%lf\n", verify(A, lenA, B, lenB));

  test(10000, 100000);
  
  free(A);
  free(B);
  return 0;
}

