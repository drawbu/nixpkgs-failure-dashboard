# Nixpkgs failure dashboard

![](./screenshot.png)

Use `./build-all-packages.sh` or `./run-build package-list.txt` to gather
build logs for the derivations.

Example:

```
echo -e "hello\nfilterpath" > example-packages-list.txt
./run-build.sh example-packages-list.txt ~/repos/nixpkgs
```

If you are in the repository, you may use the `dummy-setup` command within
the virtual environment for copy to setup the sample folder.


### Run the dashboard

*You can directly use `nix build` to skip step 1 and 2.*

1 - prepare the back
```
python -m venv venv
venv/bin/pip install -e .
```

2 - build the front
```
pnpm i
pnpm build
```

3 - create the database
```
venv/bin/classify-build-logs
```

4 - run the server
```
venv/bin/nixpkgs-failure-dashboard
```
