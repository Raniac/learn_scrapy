# Dev Notes

## Initiate Scrapy Dev Env Docker Container

```bash
$ docker run -it --rm -v /c/Users/Benny/Documents/Projects/learn_scrapy:/learn_scrapy scrapy-dev-env /bin/bash
$ cd learn_scrapy/
# $ export LANG=en_US.UTF-8 # if encountered 'UnicodeEncodeError: 'ascii' codec can't encode characters in ordinal not in range(128)'
```

## References

- [爬虫框架Scrapy的安装与基本使用](https://www.jianshu.com/p/6bc5a4641629)
- [爬虫框架Scrapy个人总结（详细）熟悉](https://www.jianshu.com/p/cecb29c04cd2)
- [INFO: Ignoring response <403 https://movie.douban.com/top250>: HTTP status code is not handled or not allowed](https://www.cnblogs.com/QW-lzm/p/9461375.html)
- [爬虫出现Forbidden by robots.txt](https://blog.csdn.net/zzk1995/article/details/51628205)
- [scrapy结合selenium进行动态加载页面内容爬取](https://www.jianshu.com/p/87ab84828a5d)
- [scrapy爬虫框架和selenium的配合使用](https://www.cnblogs.com/bk9527/p/10504883.html)