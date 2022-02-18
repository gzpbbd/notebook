

# Java 基础

## 异常

​	Exception 分类:

- RuntimeException: 运行期异常，是由代码书写错误导致的
- CheckedException：一般是外部错误（如读文件末尾数据，IO错误），这些异常都发生在编译阶段，Java 编译器会强制要求程序处理该类异常（try catch 或者 throw/throws）



# 简化编程的jar包

## lombok

maven 依赖

```xml
<dependency>
    <groupId>org.projectlombok</groupId>
    <artifactId>lombok</artifactId>
</dependency>		
```

提供了一些简化代码的注解:

```java
@Data 只能用于 Class。等价于同时使用 @Getter @Setter @RequiredArgsConstructor @ToString @EqualsAndHashCode 等注解
	注意对于 boolean 型，为了避免一些情况下的错误/歧义，生成的 getter 方法为 isXxx()
@Slf4j 生成 log 成员变量，用于记录日志
@Getter
@Setter
@ToString
@EqualsAndHashCode 生成 equals、hashCode 方法
@NoArgsConstructor
@AllArgsConstructor
```



# MySql

## 增删改查

增：

```Mysql
insert into table_name(column_1, column_2) values(value_1_1, value_1_2), (value_2_1, value_2_2)
```

删：

```Mysql
delete from table_name where condition_expression
```

改：

```mysql
update table_name set column_name = other_value where condition_expression
```

查：

```mysql
select column_name_1, column_name_2 from table_name 
	where column_name_1 = value 
	and column_name_2 between value_1 and value_2 
	and column_name_3 like 'like_expression' 
	and column_name_4 regexp 're_expression'
```





