//
//  expr.m
//  expr
//
//  Created by yaolong3 on 12-9-20.
//  Copyright (c) 2012年 yaolong3. All rights reserved.
//

/*
 http://weibo.com/1915548291/yCJDv91q4
 #谷歌面试题# #OO设计# 算数表达式由数字和操作符组成，数字包括：0，1，2，...，9；
 操作符包括：+，-，x，/。比如，10+5x78-3/42。那你怎么设计一个或多个类（class）
 来表示这种表达式。如果你有时间的话，写下你的代码，可以用长微博，图片，或是微盘展示出来。
 多多交互，多多实践，展示你的才干。
 */

#import <Foundation/Foundation.h>

@class Expr;

///////////////////////////////////////////////////////////////////////////////////////////
//节点基类
@interface ExprNode : NSObject {}
- (void)print;
- (int)eval;
@end

@implementation ExprNode
- (void)print {}
- (int)eval { return 0;}
@end

///////////////////////////////////////////////////////////////////////////////////////////
//整数节点类
@interface IntNode : ExprNode {
  int n;
}
@property (nonatomic, assign) int n;
- (id)initWithNum:(int) num;
+ (id)nodeWithNum:(int) num;
- (void)print;
- (int)eval;
@end

@implementation IntNode
@synthesize n;

- (id)initWithNum:(int)num {
  if ((self = [super init])) {
    n = num;
  }
  return self;
}

+ (id)nodeWithNum:(int)num {
  return [[[[self class] alloc] initWithNum:num] autorelease];
}

- (void)print {
  printf("%d", n);
}

- (int)eval {
  return n;
}
@end

///////////////////////////////////////////////////////////////////////////////////////////
//一元操作节点类
@interface UnaryNode : ExprNode {
  NSString *op;
  Expr *one;
}
@property (nonatomic, copy) NSString *op;
@property (nonatomic, retain) Expr *one;

- (id)initWithOperator:(NSString *)s one:(Expr *)o;
+ (id)nodeWithOperator:(NSString *)s one:(Expr *)o;
- (void)print;
- (int)eval;

@end

@implementation UnaryNode

@synthesize op, one;

- (id)initWithOperator:(NSString *)s one:(Expr *)o {
  if ((self = [super init])) {
    self.op = s;
    self.one = o;
  }
  return self;
}

+ (id)nodeWithOperator:(NSString *)s one:(Expr *)o {
  return [[[[self class] alloc] initWithOperator:s one:o] autorelease];
}

- (void)print {
  printf("(");
  printf("%s", [op cStringUsingEncoding:NSASCIIStringEncoding]);
  [one print];
  printf(")");
}

- (int)eval {
  if (op != @"-") {
    [[NSException exceptionWithName:@"zero" reason:@"wwwww" userInfo:nil] raise];
  }
  return -[one eval];
}

- (void)dealloc {
  self.op = nil;
  self.one = nil;
  [super dealloc];
}
@end

///////////////////////////////////////////////////////////////////////////////////////////
//二元操作节点类
@interface BinaryNode : ExprNode {
  NSString *op;
  Expr *one;
  Expr *two;
}
@property (nonatomic, copy) NSString *op;
@property (nonatomic, retain) Expr *one;
@property (nonatomic, retain) Expr *two;
- (id)initWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t;
+ (id)nodeWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t;
- (void)print;
- (int)eval;

@end

@implementation BinaryNode

@synthesize op, one, two;

- (id)initWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t {
  if ((self = [super init])) {
    self.op = s;
    self.one = o;
    self.two = t;
  }
  return self;
}

+ (id)nodeWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t {
  return [[[[self class] alloc] initWithOperator:s one:o two:t] autorelease];
}

- (void)print {
  printf("(");
  [one print];
  printf("%s", [op cStringUsingEncoding:NSASCIIStringEncoding]);
  [two print];
  printf(")");
}

- (int)eval {
  int op1 = [one eval];
  int op2 = [two eval];
  
  if (op == @"+") {
    return op1 + op2;
  }
  if (op == @"-") {
    return op1 - op2;
  }
  if (op == @"*") {
    return op1 * op2;
  }
  if (op == @"/" && op2 != 0) {
    return op1 / op2;
  }
  [[NSException exceptionWithName:@"operator error" reason:@"operator error" userInfo:nil] raise];
  return 0;
}

- (void)dealloc {
  self.one = nil;
  self.two = nil;
  self.op = nil;
  [super dealloc];
}
@end

///////////////////////////////////////////////////////////////////////////////////////////
//句柄类--表示一个表达式，
@interface Expr : NSObject {
  ExprNode *p;
}
@property (nonatomic, retain) ExprNode *p;
- (id)initWithNum:(int)n;
- (id)initWithOperator:(NSString *)s one:(Expr *)o;
- (id)initWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t;

+ (id)exprWithNum:(int)n;
+ (id)exprWithOperator:(NSString *)s one:(Expr *)o;
+ (id)exprWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t;

+ (id)expr:(int)n;
+ (id)expr:(NSString *)s one:(Expr *)o;
+ (id)expr:(NSString *)s one:(Expr *)o two:(Expr *)t;

- (void)print;
- (int)eval;
@end

@implementation Expr
@synthesize p;

- (id)initWithNum:(int)n {
  if ((self = [super init])) {
    p = [[IntNode alloc] initWithNum:n];
  }
  return self;
}

- (id)initWithOperator:(NSString *)s one:(Expr *)o {
  if ((self = [super init])) {
    p = [[UnaryNode alloc] initWithOperator:s one:o];
  }
  return self;
}

- (id)initWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t {
  if ((self = [super init])) {
    p = [[BinaryNode alloc] initWithOperator:s one:o two:t];
  }
  return self;
}

+ (id)exprWithNum:(int)n {
  return [[[[self class] alloc] initWithNum:n] autorelease];
}

+ (id)exprWithOperator:(NSString *)s one:(Expr *)o {
  return [[[[self class] alloc] initWithOperator:s one:o] autorelease];
}

+ (id)exprWithOperator:(NSString *)s one:(Expr *)o two:(Expr *)t {
  return [[[[self class] alloc] initWithOperator:s one:o two:t] autorelease];
}

+ (id)expr:(int)n {
  return [[[[self class] alloc] initWithNum:n] autorelease];
}

+ (id)expr:(NSString *)s one:(Expr *)o {
  return [[[[self class] alloc] initWithOperator:s one:o] autorelease];
}

+ (id)expr:(NSString *)s one:(Expr *)o two:(Expr *)t {
  return [[[[self class] alloc] initWithOperator:s one:o two:t] autorelease];
}

- (void)print {
  [p print];
}

- (int)eval {
  return [p eval];
}

- (void)dealloc {
  [p release];
  [super dealloc];
}

@end

int main(int argc, const char * argv[])
{
  
  @autoreleasepool {
    
    //10+5x78-3/42
    Expr *e = [Expr expr:@"-"
                     one:[Expr expr:@"+"
                                one:[Expr expr:10]
                                two:[Expr expr:@"*"
                                           one:[Expr expr:5]
                                           two:[Expr expr:78]
                                     ]
                          ]
                     two:[Expr expr:@"/"
                                one:[Expr expr:3]
                                two:[Expr expr:42]
                          ]
               ]
    ;
    [e print];
    printf("=%d\n", [e eval]);
    
    //e+(-8)
    e = [Expr expr:@"+" one:e two:[Expr expr:@"-" one:[Expr expr:8]]];
    [e print];
    printf("=%d\n", [e eval]);
  }
  return 0;
}

