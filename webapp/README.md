## 开发

这里使用 [pipenv](https://github.com/pypa/pipenv) 管理项目依赖，只需要执行以下命令即可使用：

```bash
# 安装所有依赖（包括测试的）
$ pipenv install --dev
# 测试（在 manage.py 所在目录运行）
$ pipenv run pytest
# 启动服务（在 manage.py 所在目录运行）
$ pipenv run python manage.py runserver
```

或者可以先用 `pipenv shell` 进入虚拟环境，然后就可以不加 `pipenv run` 了。

如果想使用一个新的干净的 Database，可以删除 `db.sqlite3` 后执行 `python manage.py migrate`，然后再执行上面最后一行 runserver 的命令即可。

如果需要安装新的依赖，使用 `pipenv install xx` 就可以将新依赖安装到已有的虚拟环境中。

部署相关可参考：[Web-Full-Stack-Practice: Web Full Stack Practice for Beginners：Docker + uWSGI + Celery + Django + Supervisor + React + Nginx + HTTPS + Postgres + Redis](https://github.com/hscspring/web-full-stack-practice)

## 文档

文档使用了 [Sphinx](http://www.sphinx-doc.org/en/master/)，使用 pip 安装好后，只需要两个命令就可以使用了

```bash
$ sphinx-quickstart
$ make html
```

第一个命令会引导你创建基本结构，然后需要在 source 下面编写 rst 文件（同时根据需要进一步配置 `conf.py`）；第二个命令会自动将 rst 文件转为 html 文档。

这里已经 make 好了，直接双击打开 `./docs/build/html/index.html` 就可以了。