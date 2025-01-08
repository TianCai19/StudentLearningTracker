"""Generate enhanced student progress report with ranking and submission dates."""

import os
from datetime import datetime
from collections import defaultdict

def parse_date_from_filename(filename):
    """Parse date from filename with error handling."""
    try:
        # 假设文件名格式为 YYYY-MM-DD.md
        date_str = filename.split(".")[0]
        return datetime.strptime(date_str, "%Y-%m-%d").date()
    except (ValueError, IndexError):
        return None

def generate_progress_report():
    """Generate markdown progress report with ranking and submission dates."""
    students_dir = "students"
    student_data = defaultdict(lambda: {
        "report_count": 0,
        "submission_dates": set(),
        "last_submission": None
    })

    if os.path.exists(students_dir):
        for student in os.listdir(students_dir):
            student_path = os.path.join(students_dir, student)
            if os.path.isdir(student_path):
                for filename in os.listdir(student_path):
                    if filename.endswith('.md'):
                        # 更新统计数据
                        student_data[student]["report_count"] += 1
                        
                        # 解析日期
                        date = parse_date_from_filename(filename)
                        if date:
                            student_data[student]["submission_dates"].add(date)
                            # 更新最后提交日期
                            if (student_data[student]["last_submission"] is None or 
                                date > student_data[student]["last_submission"]):
                                student_data[student]["last_submission"] = date

    # 生成排名
    ranked_students = sorted(
        student_data.items(),
        key=lambda x: (-x[1]["report_count"], x[0])
    )

    # 生成报告
    report_lines = [
        "# Student Progress Report",
        f"Generated at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n",
        "## Ranking\n"
    ]

    # 添加排名信息
    for rank, (student, data) in enumerate(ranked_students, 1):
        report_lines.append(f"{rank}. {student}")
        report_lines.append(f"   - Total reports: {data['report_count']}")
        report_lines.append(f"   - Submission days: {len(data['submission_dates'])}")
        if data["last_submission"]:
            report_lines.append(f"   - Last submission: {data['last_submission']}")
        report_lines.append("")

    # 保存报告
    os.makedirs("progress", exist_ok=True)
    report_path = os.path.join("progress", "progress_report.md")
    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(report_lines))

if __name__ == "__main__":
    generate_progress_report()
