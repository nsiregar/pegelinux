Requirements for development:
  * yarn: https://yarnpkg.com/en/docs/install

Install dependencies:

```
$ yarn
```

Build in development mode:

```
$ yarn build
```

Run the tests:

```
$ yarn test
```

To automatically run the tests when theres file changed:

```
$ yarn karma
```

To build with uglified js:

```
$ yarn production-build
```

The compiled javascript file is in directory app/assets/js. For the time being we commited compiled js into the scm, so the code from scm can be deployed directly to heroku. In the future, we should not commit compiled js and run the compilation as part of deployment process.
