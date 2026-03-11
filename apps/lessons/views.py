from django.shortcuts import render
from .models import (
    Lesson,
    Step,
    TheoryStep,
    ChoiceStep,
    TextInputStep,
    ProgrammingStep,
)
from django.shortcuts import get_object_or_404


def lesson_view(request, lesson_id):
    lesson = get_object_or_404(
        Lesson.objects.select_related("module__course"),
        public_id=lesson_id,
        is_published=True,
    )

    # get all steps associated with lesson
    steps = lesson.steps.all()
    # step order from query or first
    step_order = request.GET.get("step", 1)
    # find step
    current_step = get_object_or_404(Step, lesson=lesson, order=step_order)

    step_content = None
    # set content
    if current_step.type == "T":
        step_content = TheoryStep.objects.get(pk=current_step.pk)
    elif current_step.type == "C":
        step_content = ChoiceStep.objects.prefetch_related("options").get(
            pk=current_step.pk
        )
    elif current_step.type == "I":
        step_content = TextInputStep.objects.get(pk=current_step.pk)
    elif current_step.type == "P":
        step_content = ProgrammingStep.objects.prefetch_related("test_cases").get(
            pk=current_step.pk
        )

    # if htmx is used: update step_content
    if request.headers.get("HX-Request"):
        return render(
            request,
            "partials/step_content.html",
            {
                "current_step": step_content,
                "steps": steps,
                "lesson": lesson,
            },
        )

    return render(
        request,
        "lessons/lesson.html",
        {
            "lesson": lesson,
            # already in memory from select_related
            "course": lesson.module.course,
            # for sidebar
            "steps": steps,
            # for content box
            "current_step": step_content,
        },
    )


def submit_view(request, lesson_id):
    pass
