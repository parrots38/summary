# start test: execute 'pytest' in current directory
import requests


HOME = "https://todo.pixegami.io/"
PAYLOAD = {
      "content": "clean your room",
      "user_id": "mom",
      "task_id": "mom_task_1",
      "is_done": False
}

def test_can_call_root():
    response = requests.get(HOME)
    assert response.status_code == 200, "status code is not 200"

def test_can_create_task():
    create_response = create_task(PAYLOAD)
    assert create_response.status_code == 200, "status code is not 200"
    assert create_response.json()["task"], "a task didn't create"

    get_response = get_task(create_response.json()["task"]["task_id"])
    assert get_response.status_code == 200, "status code is not 200"
    assert get_response.json()["is_done"] == create_response.json()["task"]["is_done"]
    assert get_response.json()["content"] == create_response.json()["task"]["content"]
    assert get_response.json()["user_id"] == create_response.json()["task"]["user_id"]
    assert get_response.json()["task_id"] == create_response.json()["task"]["task_id"]

def test_delete_task():
    create_response = create_task(PAYLOAD)
    delete_response = delete_task(create_response.json()["task"]["task_id"])
    assert delete_response.status_code == 200, "status code is not 200"
    assert delete_response.json()["deleted_task_id"] == create_response.json()["task"]["task_id"]

def create_task(payload):
    return requests.put(HOME + "create-task/", json=payload)

def get_task(task_id):
    return requests.get(HOME + f"get-task/{task_id}")

def delete_task(task_id):
    return requests.delete(HOME + f"delete-task/{task_id}")
