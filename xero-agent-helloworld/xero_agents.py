from agents import Agent
from agents.mcp import MCPServer

def create_basic_xero_agent(mcp_server: MCPServer) -> Agent:
    """
    Create a basic Xero agent with all tools.
    
    Args:
        mcp_server: The MCP server instance for Xero
    
    Returns:
        Configured Agent instance
    """
    agent = Agent(
        name="Xero Assistant",
        model="gpt-4o-mini",
        instructions="""You are a helpful accounting assistant that manages Xero operations. 
        You can create invoices, manage contacts, search for records, and handle various 
        accounting tasks. Always confirm successful operations and provide relevant details 
        to the user. Be precise with data handling and always verify important information.""",
        mcp_servers=[mcp_server]
    )
    
    return agent


def create_invoice_specialist_agent(mcp_server: MCPServer) -> Agent:
    """
    Create an agent that specializes in invoice operations.
    
    Args:
        mcp_server: The MCP server instance for Xero
    
    Returns:
        Configured Agent instance for invoice operations
    """
    agent = Agent(
        name="Invoice Specialist",
        model="gpt-4o-mini",
        instructions="""You are an invoice specialist for Xero. You excel at creating, 
        finding, and managing invoices. You understand accounting practices and can help 
        with invoice workflows. Always provide invoice numbers and IDs when creating or 
        finding invoices.""",
        mcp_servers=[mcp_server]
    )
    
    return agent


def create_contact_manager_agent(mcp_server: MCPServer) -> Agent:
    """
    Create an agent that specializes in contact management.
    
    Args:
        mcp_server: The MCP server instance for Xero
    
    Returns:
        Configured Agent instance for contact operations
    """
    agent = Agent(
        name="Contact Manager",
        model="gpt-4o-mini",
        instructions="""You are a contact management specialist for Xero. You help create, 
        find, and update customer and supplier information. You understand the importance 
        of accurate contact data for accounting and always validate important details.""",
        mcp_servers=[mcp_server]
    )
    
    return agent

