from django.db import migrations


SKILLS = [
    # AI & Machine Learning
    ("Prompt Engineering",        "AI & Machine Learning", 1),
    ("LangChain",                 "AI & Machine Learning", 2),
    ("n8n Workflow Automation",   "AI & Machine Learning", 3),
    ("Chatbase",                  "AI & Machine Learning", 4),
    ("Google AI Studio",          "AI & Machine Learning", 5),
    ("OpenAI / Gemini AI",        "AI & Machine Learning", 6),
    ("scikit-learn",              "AI & Machine Learning", 7),
    ("Multi-Agent Orchestration", "AI & Machine Learning", 8),
    # Programming & Development
    ("Python",     "Programming & Development", 1),
    ("Django",     "Programming & Development", 2),
    ("JavaScript", "Programming & Development", 3),
    ("HTML & CSS", "Programming & Development", 4),
    ("GitHub",     "Programming & Development", 5),
    ("Render",     "Programming & Development", 6),
    # Data & Analytics
    ("pandas & seaborn",                "Data & Analytics", 1),
    ("matplotlib (Data Visualization)", "Data & Analytics", 2),
    ("Business Analytics",              "Data & Analytics", 3),
    ("Financial Reporting & Forecasting","Data & Analytics", 4),
    ("Google Sheets",                   "Data & Analytics", 5),
    ("Oracle PeopleSoft / Ignite",      "Data & Analytics", 6),
    # Operations & Administration
    ("Budget Management ($90k+)",     "Operations & Administration", 1),
    ("Event Coordination (15+/yr)",   "Operations & Administration", 2),
    ("Team Supervision & Training",   "Operations & Administration", 3),
    ("Grant Administration",          "Operations & Administration", 4),
    ("Procurement & Reimbursement",   "Operations & Administration", 5),
    ("Policy & Procedure Development","Operations & Administration", 6),
    # Communication & Strategy
    ("Social Media Management",       "Communication & Strategy", 1),
    ("Website Management",            "Communication & Strategy", 2),
    ("Technical Communication",       "Communication & Strategy", 3),
    ("Cross-functional Collaboration","Communication & Strategy", 4),
    ("Scientific Figure Design",      "Communication & Strategy", 5),
]


def seed_skills(apps, schema_editor):
    Skill = apps.get_model('main', 'Skill')
    Skill.objects.all().delete()
    Skill.objects.bulk_create([
        Skill(name=name, category=category, order=order)
        for name, category, order in SKILLS
    ])


def unseed_skills(apps, schema_editor):
    apps.get_model('main', 'Skill').objects.all().delete()


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_expand_project_add_skill'),
    ]

    operations = [
        migrations.RunPython(seed_skills, unseed_skills),
    ]
