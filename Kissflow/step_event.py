#: Step Creation
from pprint import pprint

current_steps = ["Step001", "Step002", "Step003", "Step004"]
runtime_steps = ["Step001", "Step002", "StepA", "StepB", "StepC", "Step003", "Step004"]

step_meta_changes = {
    "created": [],
    "repositioned": [],
    "renamed": [],
    "deleted": [],
}

for index, n_step in enumerate(runtime_steps):
    if n_step not in current_steps:
        payload = {"StepId": n_step, "PreviousStepId": runtime_steps[index - 1]}
        step_meta_changes["created"].append(payload)

current_steps = ["Step001", "Step002", "Step003", "StepA", "StepB", "StepC", "Step004"]
runtime_steps = ["Step001", "Step003", "StepA", "StepB", "StepC", "Step002", "Step004"]
for index, step_id in enumerate(runtime_steps):
    if step_id in current_steps and index != current_steps.index(step_id):
        payload = {"StepId": step_id, "PreviousStepId": runtime_steps[index - 1]}
        step_meta_changes["repositioned"].append(payload)

current_steps = ["Step001", "Step002", "Step003", "StepA", "StepB", "StepC", "Step004"]
runtime_steps = ["Step001", "Step002", "Step004"]
deleted_steps = list(set(current_steps) - set(runtime_steps))
for c_step in deleted_steps:
    step_meta_changes["deleted"].append({"StepId": c_step})

pprint(step_meta_changes)
