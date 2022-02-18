# 引言

SpringBoot 整合了Spring 生态的很多框架（Spring, SpringMVC, Spring Data, Spring Messaging, Spring Actuator, Spring Security, Spring WebFlux, Spring HATEOAS 等），简化了这些框架的编程。

学习的SpringBoot版本：2.6.3

- 官网：https://spring.io/projects/spring-boot#learn
- 手册（PDF版）：https://docs.spring.io/spring-boot/docs/2.6.3/reference/pdf/spring-boot-reference.pdf
- API：https://docs.spring.io/spring-boot/docs/2.6.3/api/

# 手册解读

对应的版本 2.6.3

## 目录

1. 版权

2. 寻求帮助，报告Bug与贡献代码

3. 手册总览
   - 简单指明了一些主题对应的章节：开发Web程序，操作数据库，Messaging 协议，IO，镜像

4. 使用入门（安装、开发、运行）

5. 项目如何从版本1.x.x迁移到2.x.x

### 6. 与第四章相比，更加深入介绍了SpringBoot的使用

   1. 如何构建SpringBoot工程（依赖管理，Maven，Grable，Ant，Starters）
   2. 项目的目录结构
   3. 配置类与XML配置文件
   4. 自动配置（如何 disabling 特定包的自动配置）
   5. Beans 与依赖注入
   6. @SpringBootApplication 注解
   7. 开发者工具（spring-boot-devtools 包）的介绍
   8. 打包项目

### 7. 核心特色（core features）

   1. SpringBoot程序的入口类 SpringApplication 的介绍
   2. 如何设置外部配置（propertities文件，yaml文件，系统环境变量等）
   3. Profiles
   4. Logging 的配置
   5. 国际化
   6. JSON 的整合
   7. 任务的调度（配置线程池大小）
   8. 代码测试
   9. 写自己的 Auto-configuration （写 starter）
   10. 对 Kotlin 的支持

### 8. 创建 Web 应用

   1. Servlet Web 应用
      1. SprinvMVC 框架（SpringMVC自动配置，HttpMessageConverters，定制JSON序列化与反序列化，MessageCodesResolver，静态内容，欢迎页，路径映射，模板引擎，错误处理）
      2. JAX-RS与Jersey框架
      3. 嵌入式 Servlet 容器的配置

   2. 响应式 Web 应用（Spring Webflux 框架）
   3. 优雅关闭（发起关闭后再设置一个timeout时间段，该时间段内会继续处理已存在的请求，但是不接收新的请求）
   4. Spring Security （Spring 访问控制框架）
   5. Spring Session （介绍了springboot 程序运行时自动开启配置数据存储实例：JDBC, redis 等）
   6. Spring HATEOAS（实现了 HATEOAS 规范的框架）

### 9. 整合 Spring Data 框架

   1. 整合 SQL 数据库
      1. 配置数据源
      2. 使用 JdbcTemplate
      3. 使用 JPA和Spring Data JPA
      4. Spring DATA JDBC
      5. 使用 H2 数据库的 web 控制台
      6. 使用 JOOQ
      7. 使用 R2DBC

   2. 整合 NoSQL 数据库
      1. Redis
      2. MongoDB
      3. Neo4j
      4. Solr
      5. Elasticsearch
      6. Cassandra
      7. Couchbase
      8. LDAP
      9. InfluxDB

### 10. 整合消息中间件（Messaging）

    1. JMS
    2. AMQP
    3. Apache Kafka Support
    4. RSocket
    5. Spring Integration

### 11. IO

    1. 整合 Caching（Redis 等框架）
    2. Hazelcast
    3. Quartz Scheduler
    4. 发送邮件
    5. Validation（验证）
    6. 调用远程 REST 服务（RestTemplate, WebClient）
    7. 调用 Web 服务（WebServiceTemplate）
    8. 分布式事务（JTA）

12. 容器技术（dockerfiles, Cloud Native Buildpacks）

### 13. 生产环境使用的 features（监控运行状态）

    1. 开启 features（添加 xxx-actuator-starter 就可开启这些 features）
    2. Endpoints（enabling, exposing, security, configuring, custom, health information, application information）
    3. 通过HTTP监控application
    4. 通过 JMX 监控 application
    5. 配置 Logger
    6. Metrics（支持的组件、指标，自定义metrics）
    7. Auditing（审计）
    8. HTTP tracing
    9. Process Monitoring
    10. Cloud Foundry surport

14. 部署 SpringBoot Application

    1. 部署到 Cloud
    2. 安装 SpringBoot Application （安装为 Linux/Windows 系统的二进制 service 程序）

15. Spring Boot CLI（可以运行 Groovy 脚本）

16. 编写 Build Tool Plugins （Maven, Gradle, AntLib）

### 17. How-to Guides （关于一些特定问题该如何解决）

    1. 创建、运行、定制 Spring Boot 应用
    2. 属性与配置
    3. 嵌入式 Web 服务器
    4. Spring MVC
    5. Jersey 框架
    6. HTTP 客户端
    7. 日志
    8. 数据访问（框架）
    9. 数据库初始化
    10. Messaging
    11. Batch Applications
    12. Actuator
    13. Security
    14. Hot Swapping
    15. Testing
    16. Build
    17. Traditional Deployment （使用 War 包的形式部署）

### 18. 附录 A  Common Application Properties

    1. Core, Cache, JSON, Data, Transaction, Web, Server, Security, Actuator, Devtools, Testing

19. 附录 B Configuration Metadata （给工具开发者使用的）

20.  附录 C: Auto-configuration Classes

21. 附录 D: Test Auto-configuration Annotations

22. 附录 E: 可执行 Jar 包的 format

### 23. 附录 F：依赖的版本

​    

​    


# 场景整合

## mybatis

#### 依赖

```xml
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
<dependency>
    <groupId>org.mybatis.spring.boot</groupId>
    <artifactId>mybatis-spring-boot-starter</artifactId>
    <version>2.1.3</version>
</dependency>
```

#### yaml配置

```yaml
spring:
  datasource:
    username: root
    password: mysql
    url: 'jdbc:mysql://192.168.168.128/seckill?useSSL=false'
    
mybatis:
  # 指定 xml 的位置，如果不指定，会报错误 Invalid bound statement (not found)
  mapper-locations: classpath:mapper/*.xml
  # MyBatis starter 默认不开启下划线转驼峰命名法
  configuration:
    map-underscore-to-camel-case: true
```





#### mapper xml例子

```xml
<?xml version="1.0" encoding="UTF-8" ?>
<!DOCTYPE mapper
  PUBLIC "-//mybatis.org//DTD Mapper 3.0//EN"
  "http://mybatis.org/dtd/mybatis-3-mapper.dtd">
<mapper namespace="org.mybatis.example.BlogMapper">
  <select id="selectBlog" resultType="Blog">
    select * from Blog where id = #{id}
  </select>
</mapper>
```



## 日志

```yaml
logging:
  level:
    # 定位到自己的 mapper 接口包，使得能够打印 mybatis 生成的 sql 语句	
    fit.hcp.imoocsecskill.dao: debug
```

## 数据库连接池

```yaml
spring:
  datasource:
    username: root
    password: mysql
    url: 'jdbc:mysql://192.168.168.128/seckill?useSSL=false'
    # ；连接池
    druid:
      # 开启统计功能
      filters: stat
      web-stat-filter:
        enabled: true
      stat-view-servlet:
        enabled: true
      # 设置连接池大小
      initial-size: 10
      max-active: 30
      # 默认等待时间为 0
      max-wait: 1000
```

## redis 缓存

SpringBoot内置了一个 SimpleCacheConfiguration，默认使用该缓存配置。如果存在 RedisConnectionFactory bean，就会自动配置 RedisCacheConfiguration，使用 redis 做为缓存

### 步骤

- 引入依赖(redis, cache)
- 使用 @EnableCaching 修饰主程序类，使得开启缓存
- 使用 @CacheConfig、@Cacheable、@CachePut、@CacheEvict 修饰需要使用缓存的类或方法 （只能用于 class，不能用于 interface）

### 依赖

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-redis</artifactId>
</dependency>
```

### yaml 配置

```yaml
spring:
  redis:
    host: 192.168.168.128
    password: redis
    port: 16379
  # 下面两项似乎可以不用配置
  # cache:
    # type: redis
    # 可任意命名 cache 的标记符，之后使用注解的使用需要指定对应的 cacheNames
    # cache-names: redisCache #对应一个 CacheManeger 的名字
```

### Configuration 配置

在 RedisAutoConfiguration 类中，自动生成了 StringRedisTemplate 与 RedisTemplate bean 实例

- StringRedisTemplate 默认的序列化工具是 StringRedisSerializer
- RedisTemplate 默认的序列化工具是 JdkSerializationRedisSerializer，对象会被序列化为 bytes，人类难以识别。可以修改序列化工具

```java
@Autowired
RedisTemplate<Object, Object> redisTemplate;

@PostConstruct
public void configRedisTemplate() {
    redisTemplate.setKeySerializer(RedisSerializer.string());
    redisTemplate.setHashKeySerializer(RedisSerializer.string());
    redisTemplate.setValueSerializer(RedisSerializer.json());
    redisTemplate.setHashValueSerializer(RedisSerializer.json());
}
```

### 注解

@CacheConfig：对类使用，指定类级别的公用配置，其内方法注解不需再配置对应的内容

@Cacheable：如果缓存中存在指定的 key，则读取缓存；否则执行方法，并将方法的返回值写入 redis

@CachePut：先执行方法，再将方法的返回值写入缓存。如果不指定 key，会使用所有的参数作为 key

@CacheEvict：删除缓存中指定的 key。allEntries=true 表示删除指定的cacheNames下的所有的缓存

@Cacheing：不常用。可同时添加多个 @CanchePut、@Cacheable、@CacheEvict

```java
@Service
public class UserService {
    @Autowired
    UserDao userDao;

    // 将方法的返回值写入 redis
    // 如果不指定 key，会使用所有的参数作为 key
    @CachePut(cacheNames = "redisCache", key = "'redis_user_'+#result.id")
    public User addUser(User user) {
        userDao.addUser(user);
        return user;
    }

    // 如果 redis 中操作指定的 key，则读取缓存；否则执行方法，并将方法的返回值写入 redis
    @Cacheable(cacheNames = "redisCache", key = "'redis_user_'+#id")
    public User queryById(int id) {
        return userDao.queryById(id);
    }

    @Cacheable(cacheNames = "redisCache", key = "'redis_user_'+#id")
    public int updateById(int id, String userName) {
        return userDao.updateById(id, userName);
    }

    // 删除 redis 中指定的 key // allEntries=true 表示删除指定的cacheNames下的所有的缓存
    @CacheEvict(cacheNames = "redisCache", key = "'redis_user_'+#id")
    public int deleteUserById(int id) {
        return userDao.deleteUserById(id);
    }
    
    // @Cacheing 注解：同时添加多个 @CanchePut、@Cacheable、@CacheEvict
    // @CacheConfig(cacheNames = "user")注解：对类使用，指定类级别的公用配置，其内方法注解不需再配置 cacheNames 参数
}
```

### 可用的SpEL

|     名称      |    位置    | 描述                                                         |       示例       |
| :-----------: | :--------: | :----------------------------------------------------------- | :--------------: |
|  methodName   |  root对象  | 当前被调用的方法名                                           | #root.methodname |
| Argument Name | 执行上下文 | 当前被调用的方法的参数，如findArtisan(Artisan artisan),可以通过#artsian.id获得参数 |   #artsian.id    |
|    result     | 执行上下文 | 方法执行后的返回值（仅当方法执行后的判断有效，如 unless cacheEvict的beforeInvocation=false） |     #result      |




# SpringMVC

<img src="D:\共享文件夹\github_repo\notebook\20220128_SpringBoot2笔记.assets\image-20220127170034215.png" alt="image-20220127170034215" style="zoom: 67%;" />

## 加载静态资源

- 只要静态资源放在指定路径（/static，或者 /public, /resources, /META-INF/resources）下就可以访问

- 默认情况下，静态资源是映射到了 /**。比如 /static/js/seckill.js 文件对应的url映射路径为 http://ip:port/js/seckill.js 

- 可以修改默认的静态资源映射方式，比如				

  ```yaml
  // 将 /static/js/seckill.js 文件映射到  http://ip:port/res/js/seckill.js
  spring.mvc.static-path-pattern=/res/**
  ```

- 有时候，新建的 SpringBoot web Initailizr 项目也访问不了静态资源，删除 target 文件夹，重新启动试一下

- 如果 HTML 中加载静态资源失败，先手动在浏览器中指定静态资源的访问路径试一下

- Thymeleaf 中，如果需要加载 js 文件，需要使用 th:src，如下

  ```html
  <--  加载 /static 下的 script/seckill.js 文件  -->
  <script type="text/javascript" th:src="@{/script/seckill.js}"></script>
  ```

# 事务

注解：

```java
@Transactional 声明事务，用于声明类或者方法，参数如下：
    isolation：隔离级别，是数据库自带的概念，指明数据库中数据独享的方式
    	默认为 Isolation.DEFAULT
	propagation：传播行为，是Spring引入的概念，指明事务方法调用其它方法时，其它方法如何获取事务。
    	默认为 Propagation.REQUIRED（如果有事务，就使用现有事务，否则创建新事务）
@EnableTransactionManagement 开启事务管理
```

**注意：**

- 只有程序抛出RuntimeException时，才会回滚事务；非RuntimeException不会导致事务回滚
- 如果异常在方法内部被捕获，Spring感受不到程序发送异常，因此事务不会回滚
- 需要保证事务方法的执行时间尽可能短，不要穿插其它网络操作，把其它网络操作剥离到事务方法外部

# Restful

### 操作

```
get 查询操作
post 添加/修改操作
put 修改操作
delete 删除操作
```

### URL	

```
/模块/资源/{标示}/集合1/... 
```

​	注：集合使用名词形式，而不是动词形式

​	例子：

```
/user/{uid}/frends 好友列表
/user/{uid}/followers 关注者列表
```

# Controller层注解

### @ RequestMapping注解

​	用于 URL 映射

- 支持标准的URL，
- Ant风格URL (即?和*和**等字符)
- 带{xxx}占位符的URL。

​	**例如:**

- /user/*/creation

  匹配/user/aaa/creation、/user/bbb/creation等URL。

- /user/**/creation

  匹配/user/creation、/user/aaa/bbb/creation等URL。

- /user/{userld}

  匹配user/123、user/abc等URL。

### 	获取 Request

#### 	@RequestParam

​	获取 request 中的 parameter

#### 	@RequestHeader

​	获取请求头中的数据

#### 	@CookieValue

​	获取 cookie 的数据
​    **例如：**​      

```java
@RequestMapping(value = "/getvalue")
public String list7(
        HttpServletRequest request,
        String username,
        @RequestParam(value = "id", required = false, defaultValue = "123") int id,
        @RequestHeader(value = "host") String host,
        @CookieValue(value = "JSESSIONID", required = false) String sid,
        User user
) {	
    return "home";
}	
```

### 
