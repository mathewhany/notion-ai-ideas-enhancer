from .ai_enhancer import AIEnhancer


class AITitleGenerator(AIEnhancer):
    def process(self, idea: str) -> dict[str, str]:
        prompt = f"""
        Project Idea: A platform that uses machine learning to adaptively improve students' understanding of complex math concepts through personalized problem sets.
        Project Title: MathMaster: Personalized Learning Journey

        Project Idea: A mobile app that optimizes your daily schedule, balancing productivity with well-being by using AI to suggest study times, breaks, and leisure activities.
        Project Title: OptiDay: Smart Productivity Enhancer

        Project Idea: A web tool for small to medium-sized e-commerce businesses that provides insights and analytics on customer behavior, sales trends, and inventory management.
        Project Title: InsightEcom: E-Commerce Analytics Dashboard

        Project Idea: {idea}
        Project Title: 
        """

        return {
            "title": self._generate(
                prompt,
                max_length=100,
                acceptence_criteria=lambda title: "Project Title" not in title,
            ),
        }
