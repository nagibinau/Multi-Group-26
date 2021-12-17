# IO-bound 

<img alt="sync_verification" align="left" src="https://github.com/nagibinau/Multi-Group-26/blob/main/results/verification_link.png"/> <br>

При синхронной проверке длительность достигает более 17 минут, учитывая, что объем данных мал, время очень большое. <br>
При распараллеливании потоков, заметно значительное уменьшение времени проверок — сократилось до 2-3 минут. <br>

# CPU-bound 

Поиск монет 1 воркером за 1 минуту <br>

![1_worker](https://github.com/nagibinau/Multi-Group-26/blob/main/results/1_worker_result.png)

Поиск монет 5 воркерами за 1 минуту <br>

![5_workers](https://github.com/nagibinau/Multi-Group-26/blob/main/results/5_workers_result.png)

В минуту, при 1 рабочем мы могли в среднем получить только 1 монету, но при увеличении рабочих до 5 результат генерации увеличился до 6 монет. <br>

<h3>Ресурсы</h3>

Скорость генерации обусловлена заполнением центрального процессора

При 1 воркере <br>
![1_worker](https://github.com/nagibinau/Multi-Group-26/blob/main/results/1_worker.png)

При 2 воркерах <br>
![2_workers](https://github.com/nagibinau/Multi-Group-26/blob/main/results/2_workers.png)

При 5 воркерах <br>
![5_workers](https://github.com/nagibinau/Multi-Group-26/blob/main/results/5_workers.png)
