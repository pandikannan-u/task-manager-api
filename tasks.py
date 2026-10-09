from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.auth import get_current_user
from app.database import get_db
from app.models import Task, User
from app.schemas import TaskCreate, TaskUpdate, TaskResponse

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.post(
    "/",
    response_model=TaskResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_task(
    task_data: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = Task(
        **task_data.model_dump(),
        owner_id=current_user.id,
    )

    db.add(task)
    db.commit()
    db.refresh(task)
    return task


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return (
        db.query(Task)
        .filter(Task.owner_id == current_user.id)
        .all()
    )


@router.get("/{task_id}", response_model=TaskResponse)
def get_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == current_user.id,
        )
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    return task


@router.put("/{task_id}", response_model=TaskResponse)
def update_task(
    task_id: int,
    task_data: TaskUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == current_user.id,
        )
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    for key, value in task_data.model_dump().items():
        setattr(task, key, value)

    db.commit()
    db.refresh(task)
    return task


@router.delete(
    "/{task_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    task = (
        db.query(Task)
        .filter(
            Task.id == task_id,
            Task.owner_id == current_user.id,
        )
        .first()
    )

    if task is None:
        raise HTTPException(
            status_code=404,
            detail="Task not found",
        )

    db.delete(task)
    db.commit()
    return None