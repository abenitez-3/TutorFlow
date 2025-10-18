from __future__ import annotations
import json
from typing import Any, Dict, Optional
import requests

class PersonasClient:
    def __init__(self, base_url: str, personas_endpoint: str, timeout: int = 10):
        self.base_url = base_url.rstrip("/")
        self.personas_endpoint = personas_endpoint if personas_endpoint.startswith("/") else f"/{personas_endpoint}"
        self.timeout = timeout

    # Helpers
    def _url(self, *parts: str) -> str:
        suffix = "/".join(s.strip("/") for s in parts if s is not None)
        return f"{self.base_url}{self.personas_endpoint}" + (f"/{suffix}" if suffix else "")

    def _handle(self, r: requests.Response) -> Any:
        try:
            r.raise_for_status()
        except requests.HTTPError as e:
            # Intenta extraer mensaje del backend
            msg = None
            try:
                msg = r.json()
            except Exception:
                msg = r.text
            raise RuntimeError(f"HTTP {r.status_code}: {msg}") from e
        try:
            return r.json()
        except Exception:
            return r.text

    # CRUD típicos
    def listar(self, params: Optional[Dict[str, Any]] = None) -> Any:
        r = requests.get(self._url(), params=params, timeout=self.timeout)
        return self._handle(r)

    def obtener(self, persona_id: str | int) -> Any:
        r = requests.get(self._url(str(persona_id)), timeout=self.timeout)
        return self._handle(r)

    def crear(self, data: Dict[str, Any]) -> Any:
        r = requests.post(self._url(), json=data, timeout=self.timeout)
        return self._handle(r)

    def actualizar(self, persona_id: str | int, data: Dict[str, Any]) -> Any:
        r = requests.put(self._url(str(persona_id)), json=data, timeout=self.timeout)
        return self._handle(r)

    def eliminar(self, persona_id: str | int) -> Any:
        r = requests.delete(self._url(str(persona_id)), timeout=self.timeout)
        return self._handle(r)