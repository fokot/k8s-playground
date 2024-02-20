For testing with argo install `argocd-ingress`

```
kubectl apply -f argocd-ingress.yaml
open https://argocd.127.0.0.1.nip.io/
```

or just port forward
```
kubectl port-forward svc/argocd-server -n argocd 8080:443
open https://localhost:8080/  
```

Turn on autosync `webserver` is name of app
```
argocd app set webserver --sync-policy automated
```

To create secret use
```
echo -n "boris" | base64     
```