"""Generate progress report for student coding exercises."""

import json
import os
from collections import defaultdict
from datetime import datetime


def generate_progress_report():
    """Generate and save progress report for all students.

    The report includes statistics on completed tasks, last submission date,
    and detailed task information.
    """
    # 初始化数据结构
    student_progress = defaultdict(
        lambda: {
            "total_tasks": 0,
            "completed_tasks": 0,
            "last_submission": None,
            "task_details": [],
        }
    )

    # 遍历solutions目录
    solutions_dir = "solutions"
    if os.path.exists(solutions_dir):
        for date_dir in os.listdir(solutions_dir):
            date_path = os.path.join(solutions_dir, date_dir)
            if os.path.isdir(date_path):
                for student_dir in os.listdir(date_path):
                    student_path = os.path.join(date_path, student_dir)
                    if os.path.isdir(student_path):
                        # 更新学生进度
                        student_progress[student_dir]["total_tasks"] += 1
                        student_progress[student_dir]["completed_tasks"] += 1
                        student_progress[student_dir]["last_submission"] = date_dir
                        # 统计算法题相关信息
                        task_files = os.listdir(student_path)
                        task_details = {
                            "date": date_dir,
                            "total_tasks": len(task_files),
                            "difficulty_stats": defaultdict(int),
                            "language_stats": defaultdict(int),
                        }

                        # 分析每个算法题文件
                        for task_file in task_files:
                            if task_file.endswith(".py"):
                                task_details["language_stats"]["Python"] += 1
                            elif task_file.endswith(".java"):
                                task_details["language_stats"]["Java"] += 1
                            elif task_file.endswith(".cpp"):
                                task_details["language_stats"]["C++"] += 1
                            elif task_file.endswith(".js"):
                                task_details["language_stats"]["JS"] += 1

                            # 从文件名中提取难度信息
                            if "easy" in task_file.lower():
                                task_details["difficulty_stats"]["Easy"] += 1
                            elif "medium" in task_file.lower():
                                task_details["difficulty_stats"]["Medium"] += 1
                            elif "hard" in task_file.lower():
                                task_details["difficulty_stats"]["Hard"] += 1

                        student_progress[student_dir]["task_details"].append(
                            task_details
                        )

    # 生成报告
    report = {
        "generated_at": datetime.now().isoformat(),
        "total_students": len(student_progress),
        "students": {},
    }

    for student, data in student_progress.items():
        report["students"][student] = {
            "completion_rate": data["completed_tasks"] / data["total_tasks"]
            if data["total_tasks"] > 0
            else 0,
            "last_submission": data["last_submission"],
            "total_submissions": data["completed_tasks"],
            "task_details": data["task_details"],
        }

    # 保存报告
    os.makedirs("progress", exist_ok=True)
    report_path = os.path.join("progress", "progress_report.json")
    with open(report_path, "w", encoding="utf-8") as f:
        json.dump(report, f, indent=2, ensure_ascii=False)


if __name__ == "__main__":
    generate_progress_report()
