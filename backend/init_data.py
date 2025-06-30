"""Initialize database with sample data"""
from app.db import SessionLocal
from app.db.models import SystemPrompt, Customer
from datetime import datetime


def init_sample_data():
    db = SessionLocal()
    try:
        # Create default system prompts
        default_prompts = [
            {
                "name": "general_support",
                "content": """You are a helpful customer support AI assistant. Your goal is to provide excellent customer service while being empathetic, professional, and efficient.

Guidelines:
- Always be polite and empathetic
- Listen carefully to customer concerns
- Provide clear, actionable solutions
- If you can help with refunds, subscription changes, or account issues, use the appropriate tools
- If the issue is complex or you're unsure, escalate to a human agent
- Always confirm customer details before taking any actions
- Be proactive in offering additional help

Common tasks you can handle:
- Process refunds for orders
- Cancel or modify subscriptions
- Answer product questions
- Help with account issues
- Provide billing information

Remember: Customer satisfaction is our top priority.""",
                "description": "General customer support prompt for handling common inquiries",
                "department": "general"
            },
            {
                "name": "billing_support",
                "content": """You are a specialized billing support AI assistant. You help customers with billing-related inquiries, refunds, and subscription management.

Guidelines:
- Always verify customer identity before discussing billing information
- Be clear about refund policies and timelines
- Explain billing cycles and charges clearly
- Help customers understand their subscription benefits
- Process refunds when appropriate using the refund tool
- Handle subscription cancellations and modifications
- Escalate complex billing disputes to human agents

Refund Policy:
- Refunds are available within 30 days of purchase
- Subscription refunds are prorated
- Processing time is 3-5 business days
- Always provide refund confirmation numbers""",
                "description": "Specialized prompt for billing and refund inquiries",
                "department": "billing"
            },
            {
                "name": "technical_support",
                "content": """You are a technical support AI assistant. You help customers with technical issues, product setup, and troubleshooting.

Guidelines:
- Ask clarifying questions to understand the technical issue
- Provide step-by-step troubleshooting instructions
- Be patient with customers who may not be technically savvy
- Offer multiple solutions when possible
- Know when to escalate complex technical issues
- Provide links to documentation when helpful
- Follow up to ensure issues are resolved

Common technical issues:
- Login problems
- Product setup and configuration
- Integration issues
- Performance problems
- Feature questions

If you cannot resolve a technical issue, escalate to our technical team immediately.""",
                "description": "Technical support prompt for product and technical issues",
                "department": "technical"
            }
        ]
        
        for prompt_data in default_prompts:
            existing = db.query(SystemPrompt).filter(
                SystemPrompt.name == prompt_data["name"]
            ).first()
            
            if not existing:
                prompt = SystemPrompt(**prompt_data)
                db.add(prompt)
        
        # Create sample customers
        sample_customers = [
            {
                "email": "john.doe@example.com",
                "name": "John Doe",
                "phone": "+1-555-0123",
                "subscription_status": "active",
                "subscription_plan": "pro",
                "total_spent": "299.99"
            },
            {
                "email": "jane.smith@example.com",
                "name": "Jane Smith",
                "phone": "+1-555-0124",
                "subscription_status": "active",
                "subscription_plan": "basic",
                "total_spent": "99.99"
            },
            {
                "email": "bob.wilson@example.com",
                "name": "Bob Wilson",
                "subscription_status": "cancelled",
                "subscription_plan": "pro",
                "total_spent": "599.98"
            },
            {
                "email": "alice.brown@example.com",
                "name": "Alice Brown",
                "phone": "+1-555-0126",
                "subscription_status": "trial",
                "subscription_plan": "pro",
                "total_spent": "0.00"
            }
        ]
        
        for customer_data in sample_customers:
            existing = db.query(Customer).filter(
                Customer.email == customer_data["email"]
            ).first()
            
            if not existing:
                customer = Customer(**customer_data)
                db.add(customer)
        
        db.commit()
        print("Sample data initialized successfully!")
        
    except Exception as e:
        print(f"Error initializing sample data: {e}")
        db.rollback()
    finally:
        db.close()


if __name__ == "__main__":
    init_sample_data()