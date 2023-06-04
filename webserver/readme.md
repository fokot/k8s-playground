For testing with argo

```
kubectl port-forward svc/argocd-server -n argocd 8080:443  
```

Turn on autosync `webserver` is name of app
```
argocd app set webserver --sync-policy automated
```

To create secret use
```
echo -n "boris" | base64     
```