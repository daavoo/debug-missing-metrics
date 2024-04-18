from dvclive import Live


with Live() as live:
    for i in range(3):
        live.log_metric("loss", i)
        live.next_step()
