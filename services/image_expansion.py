from typing import Dict, Any, Optional, Tuple
import requests
import base64
from PIL import Image
import io

def expand_image(
    api_key: str,
    image_data: bytes,
    canvas_size: Tuple[int, int],  # (width, height) of the new canvas
    original_image_size: Tuple[int, int], # (width, height) of the original image
    original_image_location: Tuple[int, int], # (x, y) top-left corner of original image on new canvas
    sync: bool = True
) -> Dict[str, Any]:
    """
    Expand an image beyond its original boundaries using Bria AI's image expansion API.
    
    Args:
        api_key: Bria AI API key
        image_data: Original image data in bytes
        canvas_size: The desired total size of the expanded image (width, height).
        original_image_size: The original image size (width, height).
        original_image_location: The top-left corner (x, y) of where the original image should be placed on the new canvas.
        sync: Whether to wait for results or get URLs immediately (default: True).
    """
    
    if not image_data:
        raise ValueError("Image data is required for image expansion")
    
    url = "https://engine.prod.bria-api.com/v1/image_expansion"
    
    headers = {
        'api_token': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Convert image to base64
    image_base64 = base64.b64encode(image_data).decode('utf-8')
    
    # Prepare request data according to Bria AI documentation
    data = {
        'file': image_base64,
        'canvas_size': list(canvas_size),
        'original_image_size': list(original_image_size),
        'original_image_location': list(original_image_location),
        'sync': sync
    }
    
    try:
        print(f"Making request to: {url}")
        print(f"Headers: {headers}")
        print(f"Payload: {data}")
        
        response = requests.post(url, headers=headers, json=data)
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        print(f"Response body: {response.text}")
        
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        
        result = response.json()
        print(f"Parsed JSON response: {result}")
        
        return result
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response content: {e.response.text if e.response else 'No response'}")
        raise Exception(f"Image expansion failed: HTTP {e.response.status_code} - {e.response.text if e.response else str(e)}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        raise Exception(f"Image expansion failed: Request error - {str(e)}")
    except Exception as e:
        print(f"General Error: {e}")
        raise Exception(f"Image expansion failed: {str(e)}")

def expand_image_by_url(
    api_key: str,
    image_url: str,
    canvas_size: Tuple[int, int],  # (width, height) of the new canvas
    original_image_size: Tuple[int, int], # (width, height) of the original image
    original_image_location: Tuple[int, int], # (x, y) top-left corner of original image on new canvas
    sync: bool = True
) -> Dict[str, Any]:
    """
    Expand an image from URL beyond its original boundaries using Bria AI's image expansion API.
    
    Args:
        api_key: Bria AI API key
        image_url: URL of the original image
        canvas_size: The desired total size of the expanded image (width, height).
        original_image_size: The original image size (width, height).
        original_image_location: The top-left corner (x, y) of where the original image should be placed on the new canvas.
        sync: Whether to wait for results or get URLs immediately (default: True).
    """
    
    if not image_url:
        raise ValueError("Image URL is required for image expansion")
    
    url = "https://engine.prod.bria-api.com/v1/image_expansion"
    
    headers = {
        'api_token': api_key,
        'Accept': 'application/json',
        'Content-Type': 'application/json'
    }
    
    # Prepare request data according to Bria AI documentation
    data = {
        'image_url': image_url,
        'canvas_size': list(canvas_size),
        'original_image_size': list(original_image_size),
        'original_image_location': list(original_image_location),
        'sync': sync
    }
    
    try:
        print(f"Making request to: {url}")
        print(f"Headers: {headers}")
        print(f"Payload: {data}")
        
        response = requests.post(url, headers=headers, json=data)
        print(f"Response status: {response.status_code}")
        print(f"Response headers: {dict(response.headers)}")
        print(f"Response body: {response.text}")
        
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        
        result = response.json()
        print(f"Parsed JSON response: {result}")
        
        return result
        
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
        print(f"Response content: {e.response.text if e.response else 'No response'}")
        raise Exception(f"Image expansion failed: HTTP {e.response.status_code} - {e.response.text if e.response else str(e)}")
    except requests.exceptions.RequestException as e:
        print(f"Request Error: {e}")
        raise Exception(f"Image expansion failed: Request error - {str(e)}")
    except Exception as e:
        print(f"General Error: {e}")
        raise Exception(f"Image expansion failed: {str(e)}")

# Export the functions
__all__ = ['expand_image', 'expand_image_by_url']
