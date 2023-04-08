# K8s playground

[Kubernetes Tutorial for Beginners [FULL COURSE in 4 Hours] by TechWorld with Nana](https://www.youtube.com/watch?v=X48VuDVv0do)

Ingress config and some info is little outdated, look into [official docs](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube)
To get ingress working on macos either use `minikube start --driver=hyperkit` or if not possible `minikube tunnel` but IP is then `127.0.0.1`

Install minikube like
```
brew install minikube
```

To add K8s dashboard and kubernetes-dashboard namespace run
```
minikube dashboard
```
[OpenLens](https://github.com/MuhammedKalkan/OpenLens) is also nice alternative to kubernetes dashboard

You can use `--watch` to watch for changes
```
kubectl get ingress -n kubernetes-dashboard --watch
```

To get more info use `-o wide`
```
kubectl get pod -o wide
```

Endpoint resource is dynamicly crated and it it which service is bound to which service
```
k get endpoints
```

Not mentioned in video
* Operators
* CRD (custom resource definition)
* DaemonSet
* Job
* CronJob
