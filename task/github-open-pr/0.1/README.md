# Add labels to an issue or a pull request

This `task` can be used to add labels to a github `pull request` or an `issue`.


## Install the Task

```
kubectl apply -f https://raw.githubusercontent.com/tektoncd/catalog/master/task/github-add-labels/0.1/github-add-labels.yaml
```

## Parameters

- **GITHUB_REPO**: The name of the repository where the pr will be opened. `www.github.com/tektoncd/catalog => catalog` (_e.g.:_`catalog` ).
- **GITHUB_ORG**: The name of the organization or user who owns the repository where the pr will be opened. `www.github.com/tektoncd/catalog => catalog`  (_e.g.:_`tektoncd`).
- **GITHUB_PR_TITLE**: The title of the pull request.
- **GITHUB_PR_BODY**: The title of the pull request.
- **MY_GITHUB_USERNAME**: The user who is going to open the pr.(_e.g.:_`zoey`).
- **MY_GITHUB_REPO**: The repo where the changes are implemented. `www.github.com/zoey/walkers => walkers` (_e.g.:_`walkers`).
- **MY_GITHUB_REPO**: The name of the `secret` holding the github-token 
- **GITHUB_TOKEN_SECRET_KEY**: The name of the `secret key` holding the github-token (_default:_`token`).


## Secret

* `Secret` to provide Github `access token` to authenticate to the Github.

Check [this](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line) to get personal access token for `Github`.


## Usage


This task expects a secret named github to exists, with a GitHub token in `token` with enough privileges to create a pr.

`Secrets` can be created as follows:
```
apiVersion: v1
kind: Secret
metadata:
  name: github
type: Opaque
stringData:
  token: $(personal_github_token)
```
or

```
kubectl create secret generic github --from-literal token="MY_TOKEN"
```

[This](../0.1/samples/run.yaml) can be referred to create a Taskrun.
