"""Generate simplified progress report for student coding exercises."""

import json
import os
from datetime import datetime

def generate_progress_report():
    """Generate basic progress report for all students."""
    student_progress = {}

    # 遍历solutions目录
    solutions_dir = "solutions"
    if os.path.exists(solutions_dir):
        for date_dir in os.listdir(solutions_dir):
            date_path = os.path.join(solutions_dir, date_dir)
            if os.path.isdir(date_path):
                for student_dir in os.listdir(date_path):
                    student_path = os.path.join(date_path, student_dir)
                    if os.path.isdir(student_path):
                        # 初始化学生进度
                        if student_dir not in student_progress:
                            student_progress[student_dir] = {
                                "total_tasks": 0,
                                "completed_tasks": 0,
                                "last_submission": None
                            }

                        # 更新学生进度
                        task_count = len(os.listdir(student_path))
                        student_progress[student_dir]["total_tasks"] += task_count
                        student_progress[student_dir]["completed_tasks"] += task_count
                        student_progress[student_dir]["last_submission"] = date_dir

    # 生成报告
    report = {
        "generated_at": datetime.now().isoformat(),
        "total_students": len(student_progress),
        "students": student_progress
    }

    # 保存报告
    os.makedirs("progress", exist_ok=True)
    report_path = os.path.join("progress", "progress_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)

if __name__ == "__main__":
    generate_progress_report()
